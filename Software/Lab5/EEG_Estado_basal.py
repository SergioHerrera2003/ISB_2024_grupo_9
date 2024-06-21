#PLOTEO SEÑAL EEG - Estado Basal 

#Importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

#Abrimos el archivo txt
f = open("estado_basal_verdadero_real_xd.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()
raw_data

Fs = 1000
Ts = 1/Fs
print(f" Fs = {Fs} hz\n Ts = {Ts} s")

#Leer el archivo excluyendo las 2 primeras filas 
array = np.genfromtxt("./estado_basal_verdadero_real_xd.txt", skip_header = 2)
#array[filas, columnas]
canalA4 = array[:,8] #Todas las filas de la columna 6 -> Canal A2 ECG
#Para conocer el número de filas
M = canalA4.shape[0] #shape devuelve una tupla con dimensiones del array
n = np.arange(0,M)
t = n*Ts #Vector de tiempo

# Ploteamos la lectura
plt.plot(t, canalA4, label="señal")     
plt.grid(linestyle=":")
plt.title("EEG - Estado basal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.legend(loc="upper right")
plt.xlim([0,30])
plt.show()

#Funcion de transferencia
VCC = 3.3 # Voltaje de operación
#(4 primeros canales -> n = 10 bits de resolución)
#(2 últimos canales -> n = 6 bits de resolución)
n = 10 #Número de bits del canal 
G_EEG = 41782 #Ganancia
EEG_V = (((canalA4/pow(2,n))-0.5)* VCC)/G_EEG
EEG_uV = EEG_V*pow(10,6)

# Ploteamos la lectura
plt.plot(t, EEG_uV, label="señal")     
plt.grid(linestyle=":")
plt.title("EEG (uV) - Estado basal ")
plt.xlabel("Tiempo (s)")
plt.ylabel("EEG(uV)")
plt.legend(loc="upper right")
plt.xlim([0,30])
plt.show()

plt.plot(t, EEG_uV, label="señal")     
plt.grid(linestyle=":")
plt.title("EEG(uV) - Estado basal")
plt.xlabel("Tiempo (s)")
plt.ylabel("EEG(uV)")
plt.legend(loc="upper right")
plt.xlim([0,5])
plt.show()

#Para saber la frecuencia de la señal debemos pasarlo al dominio de la frecuencia
N = 2**10                                     # 10 bits, 0-1023

signal_fft = np.fft.fft(EEG_uV, N)           # fft magtinud
signal_fft = np.round(np.abs(signal_fft),3)[0:N//2] # nos quedamos con los componente de la derecha de la FFT
signal_aux = signal_fft/signal_fft.max()     # hallamos el maximo para pasar la magnitud a escala db

with np.errstate(divide='ignore'):
    signal_fft_db = 10*np.log10(signal_aux)  # , out=signal_aux, where=signal_aux >= 0 para evitar division por zero

F_list = np.linspace(0,Fs/2, N//2)
F = np.round(F_list[np.argmax(signal_fft_db)], 1)   # argmax, encuentra el argumento max en un array

plt.plot(F_list, signal_fft_db)  #10 * np.log10(P / Pref) , decibelios
plt.text(F,0, f"{F}Hz")
plt.grid(linestyle=":")
plt.ylabel("Magnitud (db)")
plt.xlabel("Frecuencia (Hz)")
plt.title("FFT en el decibelios")
plt.xlim([0,200])
#plt.xticks(np.arange(0,200,10))
plt.show()
