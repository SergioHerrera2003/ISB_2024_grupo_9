# LABORATORIO 4: Uso de BiTalino para ECG

## Tabla de contenidos 
1. [Introducción](#introducción)
2. [Objetivos](#objetivos)
3. [Materiales y equipos](#materiales-y-equipos)
4. [Procedimiento](#procedimiento)
5. [Resultados](#resultados)
   - 5.1 [Conexión usada](#51-conexión-usada)
   - 5.2 [Video de la señal y ploteo de la señal en OpenSignal](#52-video-de-la-señal-y-ploteo-de-la-señal-en-opensignal) 
   - 5.3 [Ploteo de la señal en Python](#53-ploteo-de-la-señal-en-python)
   - 5.4 [Señal de simulación de paro cardiaco - ProSim 4](#54-señal-de-simulación-de-paro-cardiaco---prosim-4)
   
   - 5.5 [Ploteo de la señal en Python simulación paro cardiaco - ProSim 4 ](#55-ploteo-de-la-señal-en-python-de-simulación-de-paro-cardiaco---prosim-4) 
   - 5.6 [Discusiones](#56-discusiones)
6. [Conclusiones](#conclusiones)
7. [Referencias](#referencias)

---

## Introducción 
En este laboratorio, exploramos las ondas del Electrocardiograma (ECG) utilizando BiTalino. Vamos a repasar conceptos básicos para entender de qué va cada parte. Poco a poco aprenderemos de nuestro corazón y de la información que nos da su señal


### Conceptos Anatómicos
El corazón es un órgano muscular situado en la cavidad torácica, ligeramente hacia la izquierda del centro del pecho. Se divide en cuatro cámaras: dos aurículas (superiores) y dos ventrículos (inferiores). 
El corazón está conectado a los vasos sanguíneos, incluidas las arterias, que llevan sangre oxigenada desde el corazón a los tejidos del cuerpo, y las venas, que devuelven la sangre desoxigenada al corazón.
Dentro del corazón hay cuatro válvulas: la válvula tricúspide y la válvula mitral entre las aurículas y los ventrículos, y la válvula pulmonar y la válvula aórtica entre los ventrículos y las arterias. [1]


### Conceptos Fisiológicos
Ciclo Cardiaco: El ciclo cardíaco es el proceso de contracción y relajación del corazón que permite que la sangre circule por el cuerpo. Se divide en dos fases principales: sístole (contracción) y diástole (relajación).<br><br>
Electrofisiología Cardíaca: El corazón tiene un sistema eléctrico que regula su ritmo y función. Esto incluye la generación de impulsos eléctricos en el nodo sinusal, que inicia cada ciclo cardíaco, y la propagación de esos impulsos a través de las células cardiacas, lo que causa la contracción coordinada del corazón.<br><br>
Potencial de Acción Cardíaco: Es el cambio eléctrico que ocurre en las células cardiacas durante la despolarización y la repolarización. Durante la despolarización, las células se activan y se contraen, mientras que durante la repolarización, se relajan y se preparan para el siguiente ciclo.<br><br>
Registro Electrocardiográfico (ECG): Es una herramienta utilizada para registrar la actividad eléctrica del corazón. Un ECG muestra las ondas que representan la despolarización y repolarización de las diferentes partes del corazón, lo que ayuda a diagnosticar trastornos del ritmo cardíaco y otros problemas cardíacos. [2]


### Patologías frecuentes
**Enfermedad de las Arterias Coronarias (CAD):** Esta enfermedad se produce cuando las arterias coronarias, que suministran sangre al corazón, se estrechan debido a la acumulación de placa, lo que puede provocar un ataque al corazón o insuficiencia cardíaca.
Insuficiencia Cardíaca Congestiva: Es una condición en la que el corazón no puede bombear suficiente sangre para satisfacer las necesidades del cuerpo. Esto puede causar síntomas como fatiga, dificultad para respirar y acumulación de líquido en los pulmones y otras partes del cuerpo. <br>
**Enfermedad de las Válvulas Cardíacas:** Las válvulas cardíacas son estructuras que regulan el flujo sanguíneo dentro del corazón. Cuando estas válvulas no funcionan correctamente, pueden surgir problemas como estenosis (estrechamiento de la válvula), regurgitación (fuga de sangre a través de la válvula) o atresia (obstrucción total de la válvula).<br>
**Cardiomiopatía:** Se refiere a diversas enfermedades del músculo cardíaco que afectan su capacidad para bombear sangre de manera eficaz. Esto puede llevar a insuficiencia cardíaca y otros problemas cardíacos.<br>
**Arritmia Cardíaca:** Es un trastorno en el ritmo cardíaco, donde el corazón puede latir demasiado rápido, demasiado lento o de manera irregular. Esto puede causar mareos, desmayos o incluso ser potencialmente mortal si no se trata adecuadamente.<br>
**Pericarditis:** Esta es la inflamación del pericardio, una membrana delgada que rodea el corazón. Puede ser aguda o crónica y puede causar dolor en el pecho y dificultad para respirar. [3]
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_1.jpeg" width="500">
    <p>Figura 1. Patologías del corazón [3]
</div>


### Electrocardiograma (ECG)
#### Principios
El ECG se genera cuando hay movimiento de iones eléctricos a lo largo del corazón. Representa la dirección promedio de estos impulsos eléctricos.
Para su medición se utilizan dos electrodos (como mínimo) para recopilar un vector comparando el potencial de acción. El impulso puede ser positivo o negativo.
El corazón tiene un sistema eléctrico que regula su ritmo y función, incluida la generación de impulsos eléctricos en el nodo sinusal y la propagación de estos impulsos a través de las células cardiacas. Durante el ciclo cardiaco, se observan varios vectores eléctricos que representan la activación de diferentes partes del corazón, como las aurículas, el septo ventricular y las paredes ventriculares. [4]


#### Componentes y Ondas del ECG
El ECG consta de varias ondas, incluyendo la onda P (representa la despolarización auricular), el complejo QRS (representa la despolarización ventricular) y la onda T (representa la repolarización ventricular).


#### Segmentos y Intervalos del ECG
Se evalúan segmentos e intervalos específicos del ECG, como el intervalo PR (desde el inicio de la onda P hasta el inicio del complejo QRS) y el segmento ST (que indica el período de reposo entre la contracción ventricular y la repolarización).

La interpretación del ECG implica analizar la forma, la amplitud y la duración de las ondas y segmentos para detectar anomalías cardíacas, como arritmias, isquemia y trastornos de la conducción. [4]
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_2.jpeg" width="500">
    <p>Figura 2. Ondas del electrocardiograma [4]
</div>

## Objetivos 
- Ejecutar una correcta configuración de BiTalino.
- Adquirir señales biomédicas de ECG 
- Adquirir señales del Promsim4 
- Extraer la información de las señales ECG del software OpenSignals (r)evolution
- Entender los cambios fisiológicos que originan la señal ECG. 


## Materiales y equipos 
| MODELO      | DESCRIPCIÓN                | CANTIDAD |
|-------------|----------------------------|----------|
| ( R ) EVOLUTION | Kit BITalino              | 1        |
|              | Laptop o PC                | 1        |
| ProSim      | Simulador signos vitales   | 1        |
|              | Electrodos desechables     | 3        |
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_3.jpeg" height="300">
    <p>Figura 3. Kit BITalino
</div>

## Procedimiento

### 4.1 Instalación de OpenSignals
- Instalar OpenSignals (r)evolution [Descarga aquí](https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-boardkit-ble-bt)
  - Descargar la versión de 64 bits.

### 4.2 Conexión del BITalino con OpenSignals
1. Activar el Bluetooth para configurar la tarjeta BITalino.
2. Conectar la batería a la placa BITalino.
3. Encender la placa.
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_4.jpeg" height="300">
    <p>Figura 4. Manual de BiTalino [5]
</div>


4. Buscar la tarjeta BITalino.
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_5.jpeg" width="500">
    <p>Figura 5. Pantalla de Inicio OpenSignals
</div>

5. Agregar el pin “1234” que se muestra en la guía de inicio rápido.
6. Una vez listo, aparecerá de color azul la opción Enable en OpenSignals, lo que indica que el BITalino está listo para usarse.
7. Conectar los cables a A2, que es el puerto para Electrocardiograma (ECG).
8. Colocar los electrodos en los cables y posicionarlos en el lugar de la medición.
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_6.jpeg" width="500">
    <p>Figura 6. Canales del BiTalino. Usamos A2 [5]
</div>

### 4.3 Posicionamiento de los electrodos
Se utilizó la guía de BITalino “BITalino HOME-GUIDE #2 Electrocardiography (ECG) Exploring Cardiac Signals at the Skin Surface”. Según el protocolo para la derivación I, se colocaron los electrodos en las muñecas y cresta ilíaca como se muestra en la figura 7.
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_7.jpeg" width="500">
    <p>Figura 7. Posicionamiento de electrodos para la derivación I: IN+ (rojo) e IN-(negro) en las muñecas, REF (blanco) en la cresta iliaca [5]
</div>
   

| ELECTRODO  | COLOR  | POSICIÓN       |
|------------|--------|----------------|
| Referencia | Blanco | Cresta Ilíaca |
| Positivo   | Negro  | Muñeca derecha|
| Negativo   | Rojo   | Muñeca izquierda|

### 4.4 Protocolo
1. Se grabó durante 30 segundos con el usuario sin movimientos (reposo).
2. Se realizó 3 veces un ejercicio de inhalación - exhalación manteniendo cada estado por 5 segundos.
3.  Se grabó por 30 segundos luego de las respiraciones.
4.  Se realizaron 2 repeticiones de 10 Burpees salto de rana.
5. Se grabó por 30 segundos luego del ejercicio.
6. Se realizaron inhalaciones profundas (10 segundos), luego se mantuvo la respiración (10 segundos) para finalmente exhalar (10 segundos).


## Resultados 
### 5.1 Conexión usada 
De acuerdo a la guía mencionada se colocaron los electrodos de la siguiente manera:
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_8.jpeg" width="500">
    <p>Figura 8. Posición de los electrodos
</div>
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_9.jpeg" width="500">
    <p>Figura 9. Conexión de los electrodos con el BITalino
</div>

### 5.2 Video de la señal y ploteo de la señal en OpenSignal 
1. **Grabación de Baseline Inicial (30 segundos) - Estado: Reposo y Respiración Normal:** El sujeto de prueba mantuvo una respiración normal y tranquila, con baja interferencias y sin movimientos.
<div style="text-align: center;">
  <a href="https://youtu.be/hSLyqPwil7Q">
    <img src="https://img.youtube.com/vi/hSLyqPwil7Q/mqdefault.jpg" width="400" height="225">
  </a>
</div>

2. **Grabación Después del Ciclo de Respiración (30 segundos) - Estado: Pre-Ejercicio Respiratorio:** El sujeto de prueba realizó el ciclo de inhalación-sostener-exhalación-sostener tres veces, ejerció un esfuerzo respiratorio controlado.
<div style="text-align: center;">
  <a href="https://youtu.be/TwwWVFxxOTI">
    <img src="https://img.youtube.com/vi/TwwWVFxxOTI/mqdefault.jpg" width="400" height="225">
  </a>
</div>

3. **Grabación Después del Ejercicio (30 segundos) - Estado: Post-Ejercicio Intenso:** El sujeto de prueba realizó 2 repeticiones de 10 burpees.
<div style="text-align: center;">
  <a href="https://youtu.be/7clrUu7CCzI">
    <img src="https://img.youtube.com/vi/7clrUu7CCzI/mqdefault.jpg" width="400" height="225">
  </a>
</div>

4. **Grabación Después de la Retención de la Respiración (30 segundos) - Estado: Post-Retención Respiratoria:** El sujeto de prueba realizó una inhalación prolongada seguida de una retención de la respiración.
<div style="text-align: center;">
  <a href="https://youtu.be/6NPQbbjay3I">
    <img src="https://img.youtube.com/vi/6NPQbbjay3I/mqdefault.jpg" width="400" height="225">
  </a>
</div>

### 5.3 Ploteo de la señal en Python
De acuerdo a la data adquirida de OpenSignals se plotearon las señales ECG para cada caso descrito. Se observó una mayor frecuencia cardiaca luego de que el usuario realizara el ejercicio a comparación del estado inicial en reposo. 
- ECG - Reposo
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/5_ECG_RespiraciónNormal_Reposo.png" width="500">
   <img src="../../Imagenes/Lab4/Ploteos_Py/5_ECG_Reposo_FRECUENCIA.png" width="500">
</div>
<p style="text-align: center;"> Gráfica 1. Gráficas de ECG y FFT de Reposo </p>


- ECG - Después de la respiraciones profundas
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/6_ECG_DespuesRespiracionesSostenidas.png" width="500">
   <img src="../../Imagenes/Lab4/Ploteos_Py/6_ECG_DespResp_FRECUENCIA.png" width="500">
</div>
<p style="text-align: center;"> Gráfica 2. Gráficas de ECG y FFT de Respiraciones Profundas </p>

- ECG - Después de Burpees (ejercicio)
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/7_ECG_DespuesBurpees.png" width="500">
   <img src="../../Imagenes/Lab4/Ploteos_Py/8_ECG_RespDespBurpees_FRECUENCIA.png" width="500">
</div>
<p style="text-align: center;"> Gráfica 3. Gráficas de ECG y FFT Después de Ejercicio </p>

- ECG - Respiraciones después del ejercicio
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/8_ECG_RespiracionesDespuesBurpees.png" width="500">
   <img src="../../Imagenes/Lab4/Ploteos_Py/8_ECG_RespDespBurpees_FRECUENCIA.png"width="500">
</div>
<p style="text-align: center;"> Gráfica 4. Gráficas de ECG y FFT de Respiración después de Ejercicio </p>

Todos los códigos en:
[Códigos py](../../Software/Lab4)
- Archivos de los datos de las señales txt: <br>
   [Respiración Normal](../../Documentacion/Laboratorios/Lab4/ECG_respiracion_normal.txt)<br>
   [Respiración Sostenida](../../Documentacion/Laboratorios/Lab4/ECG_respiraciones_sostenidas.txt)<br>
   [Después de Ejercicio](../../Documentacion/Laboratorios/Lab4/ECG_despues_ejercicio.txt)<br>
   [Respiración después de Ejercicio](../../Documentacion/Laboratorios/Lab4/ECG_respriacion_despues_ejercicio%20.txt)

Código de ejemplo:
```python
#PLOTEO SEÑAL ECG RESPIRACIONES DESPUÉS DEL EJERCICIO

#Importamos librerias 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

#Abrimos el archivo txt
f = open("ECG_respiracion_despues_ejercicio.txt","r")
raw_data = f.readline()  # con f.read() leemos todo el contenido
f.close()
raw_data

Fs = 1000
Ts = 1/Fs
print(f" Fs = {Fs} hz\n Ts = {Ts} s")

#Leer el archivo excluyendo las 2 primeras filas 
array = np.genfromtxt("./ECG_respiracion_despues_ejercicio.txt", skip_header = 2)
#array[filas, columnas]
canalA2 = array[:,6] #Todas las filas de la columna 6 -> Canal A2 ECG
#Para conocer el número de filas
M = canalA2.shape[0] #shape devuelve una tupla con dimensiones del array
n = np.arange(0,M)
t = n*Ts #Vector de tiempo

# Ploteamos la lectura
plt.plot(t, canalA2, label="señal")     
plt.grid(linestyle=":")
plt.title("ECG - Respiraciones después de Burpees")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mV)")
plt.xlim([10,15])
plt.legend(loc="upper right")
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
```
### 5.4 Señal de simulación de paro cardiaco - ProSim 4 
**Conexión usada:** 
<div align="center">
   <img src="../../Imagenes/Lab4/Figura_10.jpeg" height="400">
    <p>Figura 10. Conexión de SimPro con el BITalino
</div>

**Video de la señal y ploteo de la señal en OpenSignal:**
1. **Grabación de la Contracción Ventricular Prematura (CVP) - ECG**: La grabación muestra la actividad eléctrica del corazón durante la presencia de una contracción ventricular prematura (CVP), que es un tipo de anomalía cardíaca.
   <div style="text-align: center;">
     <a href="https://youtu.be/o_2J0r7f2XY">
       <img src="https://img.youtube.com/vi/o_2J0r7f2XY/mqdefault.jpg" width="400" height="225">
     </a>
   </div>

2. **Grabación de la Taquicardia Ventricular - ECG**: Esta grabación muestra un electrocardiograma que indica taquicardia ventricular, una arritmia cardíaca caracterizada por un ritmo cardíaco rápido y anormal que comienza en los ventrículos del corazón.
   <div style="text-align: center;">
     <a href="https://youtu.be/XNoQcYaHo2o">
       <img src="https://img.youtube.com/vi/XNoQcYaHo2o/mqdefault.jpg" width="400" height="225">
     </a>
   </div>

3. **Grabación de la Fibrilación Ventricular Severa - ECG**: Esta grabación muestra un electrocardiograma que indica fibrilación ventricular severa, una arritmia potencialmente mortal caracterizada por contracciones descoordinadas y rápidas de los ventrículos del corazón.
   <div style="text-align: center;">
     <a href="https://youtu.be/6HHVxNpfxvw">
       <img src="https://img.youtube.com/vi/6HHVxNpfxvw/mqdefault.jpg" width="400" height="225">
     </a>
   </div>

4. **Grabación de la Asistolia - ECG**: Esta grabación muestra un electrocardiograma que indica asistolia, la ausencia total de actividad eléctrica y contracción muscular en el corazón, una forma extrema de paro cardíaco que requiere reanimación cardiopulmonar inmediata.
   <div style="text-align: center;">
     <a href="https://youtu.be/kOsHdmJgdE4">
       <img src="https://img.youtube.com/vi/kOsHdmJgdE4/mqdefault.jpg" width="400" height="225">
     </a>
   </div>

### 5.5 Ploteo de la señal  en Python de simulación de paro cardiaco - ProSim 4 
De acuerdo a la data adquirida de OpenSignals se plotearon las señales ECG para cada paso. En este caso de simulador de paro cardiaco. 

- ECG - Contracción Ventricular Prematura (CVP)
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/1_PASO2_CVP_PROSIM.png" >
   <img src="../../Imagenes/Lab4/Ploteos_Py/1_PASO2_FRECUENCIA.png" >
</div>
<p style="text-align: center;"> Gráfica 5. Gráficas de ECG y FFT de Contracción Ventricular Prematura </p>

- ECG - Taquicardia Ventricular 160 lpm
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/2_PASO3_TaquicardiaVentricular_PROSIM.png">
   <img src="../../Imagenes/Lab4/Ploteos_Py/2_PASO3_FRECUENCIA.png" >
</div>
<p style="text-align: center;"> Gráfica 6. Gráficas de ECG y FFT de Taquicardia Ventricular </p>

- ECG - Fibrilación Ventricular Severa
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/3_PASO4_FibrilaciónVentricularSevera_PROSIM.png" >
   <img src="../../Imagenes/Lab4/Ploteos_Py/3_PASO4_FRECUENCIA.png"  >
</div>
<p style="text-align: center;"> Gráfica 7. Gráficas de ECG y FFT de Fibrilación Ventricular Severa </p>

- ECG - Asistolia
<div style="display: flex; justify-content: center;">
   <img src="../../Imagenes/Lab4/Ploteos_Py/4_PASO5_Asitolia_PROSIM.png" >
   <img src="../../Imagenes/Lab4/Ploteos_Py/4_PASO5_FRECUENCIA.png" >
</div>
<p style="text-align: center;"> Gráfica 8. Gráficas de ECG y FFT de Asistolia </p>

Todos los códigos en:
[Códigos py](../../Software/Lab4)
- Archivos de los datos de las señales txt: <br>
   [ECG - CVP](../../Documentacion/Laboratorios/Lab4/paso2_prosim.txt)<br>
   [ECG - Taquicardia](../../Documentacion/Laboratorios/Lab4/paso3_prosim.txt)<br>
   [ECG - Fibrilación](../../Documentacion/Laboratorios/Lab4/paso4_prosim.txt)<br>
   [ECG - Asistolia](../../Documentacion/Laboratorios/Lab4/paso5_prosim.txt)

### 5.6 Discusiones
En la primera experiencia, al analizar la señal EKG durante la respiración normal, se observaron aproximadamente 7 pulsaciones en un lapso de 5 segundos, lo que equivale a una frecuencia cardíaca de alrededor de 84 pulsaciones por minuto. Este valor es consistente con una frecuencia cardíaca en reposo típica.

Después del ciclo completo de inhalación y exhalación, la señal EKG mostró aproximadamente 6 pulsaciones en 5 segundos, lo que corresponde a una frecuencia cardíaca de alrededor de 72 pulsaciones por minuto. Esta disminución en la frecuencia cardíaca esta relacionada con una adaptación fisiológica durante la respiración controlada.

En contraste, durante el ploteo de la señal EKG mientras se realizaba ejercicio, se observó un aumento significativo en la frecuencia cardíaca, con alrededor de 11 pulsaciones en 5 segundos, lo que se traduce en una frecuencia cardíaca de aproximadamente 132 pulsaciones por minuto. Este aumento es típico durante el ejercicio físico debido al aumento en la demanda metabólica del cuerpo.

Finalmente, después del ciclo de respiración controlada, la frecuencia cardíaca mostró una disminución notable, con alrededor de 8 pulsaciones en 5 segundos, lo que equivale a una frecuencia cardíaca de aproximadamente 96 pulsaciones por minuto. 

Los resultados obtenidos a través del software del BITalino del experimento realizado para medir el Electrocardiograma (ECG) y utilizando el ProSim 4 de Fluke nos muestran las respuestas fisiológicas del cuerpo, específicamente las señales de los biopotenciales relacionados al sistema circulatorio, ante diferentes estímulos.
 
**Experiencia con el BITalino**<br>
En la fase de reposo, se observaron ondas ECG normales del sujeto de prueba. Un ecg normal está formado por una onda P, un complejo QRS y una onda T [2]. Estos elementos que se pudieron identificar en este estado. También, se observa una frecuencia cardíaca, con poca variabilidad en la señal. Esto se utilizó para comparar las respuestas del corazón ante los estímulos posteriores [7].

Posteriormente se realizaron ejercicios de inhalación y exhalación controladas, se observaron cambios en el ECG asociada con la respiratoria. Durante la exhalación, el intervalo R-R que se observa en la Fig. x se alarga en comparación a la variación del intervalo durante la inhalación. 

<div align="center">
   <img src="../../Imagenes/Lab4/Figura_11.jpeg" width="500">
    <p>Figura 11. ECG y trazado respiratorio profundo.
</div>
Este fenómeno se conoce como arritmia sinusal respiratoria y se debe a la modulación del nodo sinoauricular por el sistema nervioso autónomo. Durante la inhalación, aumenta el tono simpático y disminuye el tono vagal, lo que acelera el ritmo cardíaco. Por otro lado, durante la exhalación, disminuye el tono simpático y aumenta el tono vagal, lo que desacelera el ritmo cardíaco [6]. <br>
Posteriormente, tras la realización de los Burpees, se registró un aumento en la frecuencia cardíaca en el ECG. Se debe a que el corazón responde a la demanda metabólica de los músculos del cuerpo, por lo que aumenta su actividad [7].
<br><br>

**Experiencia ProSim 4** <br>
Durante una Contracción Ventricular Prematura (PVC), se puede observar en el EKG la presencia de complejos QRS prematuros y anormales que aparecen antes de lo esperado en el ciclo cardíaco normal. Estos complejos QRS son más anchos y distintos en comparación con los complejos normales. Se observan 4 PCV en el ploteo de la señal, donde la mayoría estan precedidas por una onda P, pero no continua con una onda T, lo que puede indicar repolarización ventricular anormal.

En el caso de una Taquicardia Ventricular (TV), el EKG muestra una serie continua de complejos QRS anchos y regulares, se tienen alrededor de 53 pulsaciones en una duración de 20 segundos, lo que equivale a una frecuencia cardíaca aproximada de 160 latidos por minuto (lpm). En este paso, los complejos QRS en la TV son característicamente más anchos debido a la activación anormal de los ventrículos.

En el caso de una Fibrilación Ventricular (FV), el ploteo de la señal EKG muestra una actividad eléctrica caótica y desorganizada en los ventrículos, se aprecian una serie líneas o picos trazados de manera caotica y desordenada. No se observan complejos QRS definidos ni patrones claros de ondas P y T.

Finalmente, en el caso de la Asistolia, la señal EKG del ploteo muestra una línea casi plana con ligera presencia de ruido, indicando la ausencia total de actividad eléctrica efectiva en el corazón. Para este último paso, no se aprecian complejos QRS ni actividad eléctrica discernible en el trazado del ploteo.

## Conclusiones 
En esta experiencia, se exploró la actividad eléctrica del corazón  mediante la mediciones del ECG en diferentes condiciones, utilizando un BITalino para registrar los datos y el ProSim 4 para simular un infarto. El BITalino es un dispositivo que permite obtener mediciones del ECG mediante su software OpenSignals. Mediante el software, se observaron gráficas del ECG en diferentes situaciones. Durante el reposo, se observaron patrones cardiacos normales, es decir, ritmos regulares y consistentes. Sin embargo, al realizar el ejercicio de respiración, se observó cambios en las señales del ECG, como la variabilidad del segmento R-R, que indica una respuesta fisiológica.

Al simular un infarto en el ProSim 4 de fluke, se pudo observar alteraciones en el ECG que indican daño cardiaco, como la elevación del segmento ST. Se resalta que el ECG puede ser utilizado para la detección de sutiles alteraciones de la actividad cardiaca y la importancia de la simulación para mejorar la comprensión de las patologías relacionadas [8].


## Referencias
[1] Meu Vall d'Hebron. “Anatomía del corazón”. Hospital Universitario Vall d'Hebron. Accedido el 21 de abril de 2024. [En línea]. Disponible: https://hospital.vallhebron.com/es/asistencia/consejos-de-salud/anatomia-del-corazon#:~:text=El%20corazón%20está%20formado%20por,hay%20una%20válvula%20llamada%20auriculoventricular.

[2] Guyton, A. C., y J. E. Hall.  14ª Edición «El corazón». En Manual de fisiología médica. Madrid y Barcelona: McGraw-Hill, 2021, 115-127.

[3] UDMI. “Am I at Risk for Cardiovascular Disease? - University Diagnostic Medical Imaging”. University Diagnostic Medical Imaging. Accedido el 21 de abril de 2024. [En línea]. Disponible: https://www.udmi.net/cardiovascular-disease-risk/ 

[4] ECG and ECHO Learning. “ECG interpretation: Characteristics of the normal ECG (P-wave, QRS complex, ST segment, T-wave) – Cardiovascular Education”. Cardiovascular Education. Accedido el 21 de abril de 2024. [En línea]. Disponible: https://ecgwaves.com/topic/ecg-normal-p-wave-qrs-complex-st-segment-t-wave-j-point/

[5] ““BITalino (r)evolution Lab Guide.””. Support PLUX Biosignals official – Official PLUX support and biosignals knowledge base. Accedido el 21 de abril de 2024. [En línea]. Disponible: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide5_ACC.pdf

[6] ​​C. J. Levin, S. J. Swoap, "The impact of deep breathing and alternate nostril breathing on heart rate variability: a human physiology laboratory," Advances in Physiology Education, vol. 43, no. 3, pp. 270-276, 2019.

[7] E. M. Rad et al., "Exercise-induced electrocardiographic changes after treadmill exercise testing in healthy children: A comprehensive study," Annals of Pediatric Cardiology, vol. 14, no. 4, pp. 449-458, 2021.

[8] Ribeiro, A.H., Ribeiro, M.H., Paixão, G.M.M. et al., "Automatic diagnosis of the 12-lead ECG using a deep neural network," Nat Commun, vol. 11, no. 1, p. 1760, Apr. 2020. [Online]. Available: https://doi.org/10.1038/s41467-020-15432-4.

