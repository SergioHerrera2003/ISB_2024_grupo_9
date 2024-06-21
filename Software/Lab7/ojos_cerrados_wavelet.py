import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pywt
import statistics as s
import math as m

# Cargar datos desde el archivo txt
file_path = r"SIGNALS_EEG\ojos_cerrados.txt"  # Ruta del archivo
array = np.genfromtxt(file_path, skip_header=2)
canalA4 = array[:, 8]  # Todas las filas de la columna 8

# Frecuencia de muestreo
fs = 1000  # Frecuencia de muestreo en Hz
num_samples = canalA4.shape[0]  # Número de muestras
duration = num_samples / fs  # Duración total de la señal en segundos

# Generar el vector de tiempo
time = np.arange(0, duration, 1 / fs)  # Tiempo en segundos

# Preprocesamiento del voltaje
VCC = 3.3  # Voltaje de operación
n = 10  # Número de bits del canal
EEG_V = (((canalA4 / pow(2, n)) - 0.5) * VCC) / num_samples
EEG_signal = EEG_V * pow(10, 6)

# Duración de la ventana en segundos
window_duration = 21  # segundos
window_samples = window_duration * fs  # número de muestras en la ventana de 21 segundos

# Cortar la señal a los primeros 21 segundos
EEG_signal_21s = EEG_signal[:window_samples]
time_21s = time[:window_samples]

# Definir las frecuencias de corte del filtro pasabanda
lowcut = 0.5  # Frecuencia de corte baja en Hz
highcut = 35  # Frecuencia de corte alta en Hz
nyquist = 0.5 * fs
low = lowcut / nyquist
high = highcut / nyquist

# Diseñar el filtro Butterworth pasabanda
N_ord = 4
b, a = signal.butter(N_ord, [low, high], btype='band')

# Aplicar el filtro a la señal de 21 segundos
filtered_signal_21s = signal.lfilter(b, a, EEG_signal_21s)

# Graficar la señal original y la señal filtrada
plt.figure(figsize=(12, 6))
plt.plot(time_21s, EEG_signal_21s, label='Señal EEG Original (Primeros 21s)')
plt.xlim(0, 21)
plt.title('Señal EEG Original (Primeros 21s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.legend()

plt.figure(figsize=(12, 6))
plt.plot(time_21s, filtered_signal_21s, label='Señal EEG Filtrada (0.5-35 Hz)', color='red')
plt.xlim(0, 21)
plt.title('Señal EEG Filtrada (0.5-35 Hz) - Primeros 21s')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.legend()

plt.tight_layout()
plt.show()

# Aplicar la DWT
niveles = 5
coeficientes = pywt.wavedec(filtered_signal_21s, 'db4', level=niveles)

def calculate_global_threshold(coeffs, sigma):
    # Calcular el umbral global como un múltiplo de la desviación estándar del ruido
    Tg = sigma * m.sqrt(2 * m.log(len(filtered_signal_21s)))
    return Tg

# Aplicar umbralización suave adaptativa a todos los coeficientes
# Calcular el umbral global basado en la desviación estándar del ruido
sigma = np.median(np.abs(coeficientes[-1])) / 0.6745
threshold = calculate_global_threshold(coeficientes[-1], sigma)

# Aplicar umbralización suave adaptativa solo a los coeficientes de detalle
coeffs_thresh = [coeficientes[0]] + [pywt.threshold(detail, threshold, mode='soft') for detail in coeficientes[1:]]

# Graficar la señal original y los coeficientes de detalle
plt.figure(figsize=(10, 10))

# Graficar la señal original
plt.subplot(niveles + 1, 1, 1)
plt.plot(time_21s, filtered_signal_21s)
plt.xlim(0,21)
plt.title('Señal Original')

# Graficar los coeficientes de detalle
for i, detalle in enumerate(coeficientes[1:]):  # Empezar desde el segundo nivel
    plt.subplot(niveles + 1, 1, i + 2)  # número de subgráficos
    tiempo_detalle = time_21s[:len(detalle)]
    plt.plot(tiempo_detalle, detalle)
    plt.xlim(0, tiempo_detalle[-1])  # Limitar el eje x hasta el último tiempo del detalle
    plt.title(f'Detalle Nivel {i+1}')

# Graficar el coeficiente de aproximación
plt.subplot(niveles + 1, 1, niveles + 1)  # número de subgráficos
plt.plot(time_21s[:len(coeficientes[0])], coeficientes[0])  # Limitar el tiempo para el coeficiente de aproximación
plt.title(f'Aproximación Nivel {niveles}')

plt.tight_layout()
plt.show()

# Graficar la señal original y los coeficientes de detalle
plt.figure(figsize=(10, 10))

# Graficar la señal original
plt.subplot(niveles + 1, 1, 1)
plt.plot(time_21s, filtered_signal_21s)
plt.xlim(0,21)
plt.title('Señal Original')

# Graficar los coeficientes de detalle
for i, detalle in enumerate(coeffs_thresh[1:]):  # Empezar desde el segundo nivel
    plt.subplot(niveles + 1, 1, i + 2)  # número de subgráficos
    tiempo_detalle = time_21s[:len(detalle)]
    plt.plot(tiempo_detalle, detalle)
    plt.xlim(0, tiempo_detalle[-1])  # Limitar el eje x hasta el último tiempo del detalle
    plt.title(f'Detalle Nivel {i+1}')

# Graficar el coeficiente de aproximación
plt.subplot(niveles + 1, 1, niveles + 1)  # número de subgráficos
plt.plot(time_21s[:len(coeffs_thresh[0])], coeffs_thresh[0])  # Limitar el tiempo para el coeficiente de aproximación
plt.title(f'Aproximación Nivel {niveles}')

plt.tight_layout()
plt.show()

# Reconstruir la señal
x_rec = pywt.waverec(coeffs_thresh, 'db4')

# Graficar la señal original y la señal reconstruida en un solo gráfico
plt.figure(figsize=(12, 6))
plt.plot(time_21s, EEG_signal_21s, label='Señal EEG Original', color='blue')
plt.xlim(0, 21)
plt.ylim(-75, 75)
plt.title('Señal EEG Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')

plt.figure(figsize=(12, 6))
plt.plot(time_21s, x_rec, label='Señal Reconstruida', color='red')
plt.xlim(0, 21)
plt.ylim(-75, 75)
plt.title('Señal EEG Reconstruida')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (uV)')
plt.legend()
plt.show()
