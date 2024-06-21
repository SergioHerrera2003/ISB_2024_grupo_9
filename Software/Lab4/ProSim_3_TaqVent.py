#PLOTEO SEÑAL PASO 3 - TAQUICARDIA VENTRICULAR 160 LPM

#Importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

#Abrimos el archivo txt
f = open("paso3_prosim.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()
raw_data

Fs = 1000
Ts = 1/Fs
print(f" Fs = {Fs} hz\n Ts = {Ts} s")

#Leer el archivo excluyendo las 2 primeras filas 
array = np.genfromtxt("./paso3_prosim.txt", skip_header = 2)
#array[filas, columnas]
canalA2 = array[:,6] #Todas las filas de la columna 6 -> Canal A2 ECG
#Para conocer el número de filas
M = canalA2.shape[0] #shape devuelve una tupla con dimensiones del array
n = np.arange(0,M)
t = n*Ts #Vector de tiempo

# Ploteamos la lectura
plt.plot(t, canalA2, label="señal")     
plt.grid(linestyle=":")
plt.title("Taquicardia Ventricular 160 lpm")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.legend(loc="upper right")
plt.xlim([0,20])
plt.show()


#Para saber la frecuencia de la señal debemos pasarlo al dominio de la frecuencia
N = 2**10                                     # 10 bits, 0-1023

signal_fft = np.fft.fft(canalA2, N)           # fft magtinud
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


