import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Cargar datos desde el archivo txt
file_path = r"EEG\SIGNALS\ciclo_ojos_abiertos_cerrados (1).txt"  # Ruta del archivo
array = np.genfromtxt(file_path, skip_header=2)
canalA4 = array[:,8] # Todas las filas de la columna 6 -> Canal A2 ECG

# Genera una señal de ejemplo (simulación de señal EEG)
fs = 5000  # Frecuencia de muestreo en Hz
num_samples = canalA4.shape[0]  # Número de muestras
time = np.arange(0, num_samples / fs, 1 / fs)  # Tiempo en segundos

VCC = 3.3  # Voltaje de operación
n = 10  # Número de bits del canal
EEG_V = (((canalA4 / pow(2, n)) - 0.5) * VCC) / num_samples
EEG_uV = EEG_V * pow(10, 6)

# Convertir las frecuencias a frecuencias normalizadas
fc = 30  # Frecuencia de corte en Hz
fc_norm = fc / (fs / 2)
wp = 94  # Frecuencia de paso en rad/s
ws = 157  # Frecuencia de parada en rad/s

# Determinar el orden del filtro
N_ord, Wc = signal.buttord(wp, ws, gpass=3, gstop=40, analog=False)

# Diseñar el filtro Butterworth
b, a = signal.iirfilter(N_ord, fc_norm, btype='low', ftype='butter')

# Aplicar el filtro a la señal EEG
filtered_signal = signal.lfilter(b, a, EEG_uV)

# Graficar toda la señal EEG original
plt.figure(figsize=(10, 6))
plt.plot(time, EEG_uV, label='Señal EEG original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.xlim(0, 5)
plt.title('Señal EEG original')
plt.legend()
plt.grid(True)
plt.show()

# Graficar toda la señal EEG filtrada
plt.figure(figsize=(10, 6))
plt.plot(time, filtered_signal, label='Señal EEG filtrada', color='orange')
plt.xlabel('Tiempo (s)')
plt.xlim(0, 5)
plt.ylabel('Amplitud (uV)')
plt.title('Señal EEG filtrada')
plt.legend()
plt.grid(True)
plt.show()