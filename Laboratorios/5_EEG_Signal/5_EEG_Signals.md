# LABORATORIO 5 - MEDICIÓN DE SEÑAL EEG

## TABLA DE CONTENIDOS

- [Introducción del laboratorio](#introducción-del-laboratorio)
- [Objetivos](#objetivos)
- [Materiales y equipos](#materiales-y-equipos)
- [Procedimiento](#procedimiento)
- [Desarrollo experimental](#desarrollo-experimental)
- [Discusión y conclusiones](#discusión-y-conclusiones)
- [Referencias](#referencias)

## Introducción del laboratorio

En 1875, se registraron los primeros experimentos en neurofisiología realizados en animales por Richard Caton, quien sentó las bases en este campo. Posteriormente, en 1924, Hans Berger, psiquiatra alemán, reconoció la importancia de los avances de Caton en sus estudios sobre las ondas Alfa del cerebro [1]. El electroencefalograma (EEG) es un instrumento para medir los potenciales que se generan por la actividad cerebral. Se utiliza para estudiar la actividad del cerebro, principalmente para evaluar a pacientes para detectar convulsiones y epilepsia. A pesar de que las técnicas de imágenes avanzadas se utilizan para el diagnóstico, el EEG sigue siendo una herramienta efectiva para la detección de convulsiones [2].

El EEG también se ha incorporado en algunas clínicas para apoyarse del equipo en diferentes aplicaciones. Por ejemplo, en procedimientos quirúrgicos, el EEG puede medir el estado de sueño del paciente, para asegurar la correcta administración del la anestesia. También, se observó su utilidad para el monitoreo de isquemia o infarto, debido a su sensibilidad para detectar cambios potenciales. Además, se utiliza para la investigación de patologías mediante el análisis del funcionamiento visual, auditivo y cognitivo [2].

Para la obtención de las señales de EEG, se utilizan electrodos que se colocan en el cuero cabelludo. Los electrodos detectan potenciales generados por las neuronas corticales y ayudan a entender la interacción entre la corteza cerebral y las estructuras subcorticales. Además de caracterizar las frecuencias de onda específicas, como alfa, beta, theta y delta, también revela componentes, como los husos del sueño y los complejos K, que se utilizan para diferenciar las etapas del sueño y proporcionar información crucial sobre la actividad cerebral [1].

## Objetivos
- Adquirir señales biomédicas de EEG
- Hacer una correcta configuración de BiTalino y del Ultracortex Mark IV
- Extraer la información de las señales EEG del software OpenSignals (r)evolution y OpenBCI

## Materiales y equipos

| Cantidad | Equipo/Material          |
|----------|--------------------------|
| 1        | Kit BiTalino (R)EVOLUTION|
| 1        | Ultracortex Mark IV      |
| 1        | Laptop o PC              |
| 3        | Electrodos               |

## Procedimiento

1. **Instalación de OpenSignals**
- Instalar [OpenSignals (r)evolution](https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-boardkit-ble-bt) <br>
   Downloads -> OpenSignals -> Download 64
   

2. **Conexión del BITalino con OpenSignals**
- Activar el Bluetooth para configurar la tarjeta BITalino
- Conectar la batería a la placa BITalino
- Encender la placa 

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_1.jpeg" height="300">
    <p>Figura 1. Manual de BiTalino [3]
</div>

- Buscar la tarjeta BITalino 
<div align="center">
   <img src="../../Imagenes/Lab5/Figura_2.jpeg" height="300">
    <p>Figura 2. Pantalla de Inicio OpenSignals
</div>

- Agregar el pin “1234” que se muestra en la guía de inicio rápido
- Listo aparecerá de color azul la opción Enable en OpenSignals lo que indica que el BITalino está listo para usarse. 
- Conectamos los cables a A2 que es el puerto para Electroencefalograma (EEG)  [User Manual]
- Colocar los electrodos en los cables y ponerlos en el lugar de la medición. 
<div align="center">
   <img src="../../Imagenes/Lab5/Figura_3.jpeg" height="300">
    <p>Figura 3. Canales del BiTalino. Usamos A4 [3]
</div>

3. **Posicionamiento de los electrodos**

Se utilizó como guía para la colocación de electrodos al BITalino “BITalino HOME-GUIDE #3 ELECTROENCEPHALOGRAPHY (EEG) Exploring Brain Signals”. Según su protocolo, se colocaron los electrodos en las muñecas y cresta ilíaca como se muestra en la figura 4. 
<div align="center">
   <img src="../../Imagenes/Lab5/Figura_4.jpeg" height="300">
    <p>Figura 4. Posicionamiento de electrodos para medir EEG en la posición FP1: Pines de medición IN+/- (en la frente) y referencia (atrás de la oreja). [3]
</div>

4. **Protocolo del laboratorio**
   - Registrar una línea base de señal con poco ruido durante 30 segundos.
   - Realizar un ciclo de ojos abiertos y cerrados, manteniendo ambas fases durante cinco segundos.
   - Realizar una fase de referencia adicional, 30 segundos.
   - Realizar ejercicios mentales mientras se registran las señales, enfocando la mirada en un punto fijo.
   - Guardar los datos

> En nuestro grupo, no se tuvo el tiempo suficiente para llegar a hacer la práctica con el Ultracortex, sin embargo nos colaboraron con sus datos el grupo 9. Desde aquí, les sugerimos visiten también su página para una mayor información directa. Describiremos esas partes con el txt brindado
5. **Instalación de OpenBCI GUI**
- Instalar [OpenBCI GUI:](https://openbci.com/downloads ) <br>
   Downloads -> OPENBCI GUI v5.2.2 -> Download 64
6. **Conexión del OpenBCI GUI con Ultracortex Mark IV**
- Conectar el ultracortex con el software del OpenBCI para poder empezar a sensar los datos
- Seguir el mismo protocolo del laboratorio para cada medición de señal del EEG


## Desarrollo experimental

### Fotos de conexión usada (Electrodos-cuerpo/cabeza)

Se presenta las conexión de los electrodos en la cabeza

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_5.jpeg" height="300">
    <p>Figura 5. Foto de la conexión del Electrodos en la cabeza positiva y negativa, con la referencia para el BiTalino
</div>

### Video de señal con Bitalino
- **Línea de Base (en relajación y respirando):** El sujeto de prueba mantuvo una respiración normal y tranquila, con baja interferencias y sin movimientos.
<div style="text-align: center;">
  <a href="link">
    <img src="link" width="400" height="225">
  </a>
</div>

- **Ciclo de Ojos Abiertos - Ojos Cerrados:** El sujeto de prueba empezó con los ojos abiertos durante 5 segundos y luego los cerro durante otros 5 segundos en un ciclo.
<div style="text-align: center;">
  <a href="link">
    <img src="link" width="400" height="225">
  </a>
</div>

- **Segunda Línea de Base:** El sujeto de prueba mantuvo una respiración normal y tranquila, con baja interferencias y sin movimientos por segunda vez.
<div style="text-align: center;">
  <a href="link">
    <img src="link" width="400" height="225">
  </a>
</div>

- **Resolviendo mentalmente ejercicios:** El sujeto de prueba tuvo 12 segundos para pensar en distintos problemas matemáticos 3 Sencillos y 3 Complicados [4]
<div style="text-align: center;">
  <a href="link">
    <img src="link" width="400" height="225">
  </a>
</div>

### Ploteo de la señal en OpenSignals
- **Señal ploteada Basal 1**

  <div align="center">
     <img src="../../Imagenes/Lab5/Figura_6.jpeg" height="300">
      <p>Figura 6. Señal ploteada en estado de relajación como línea base primera medición
  </div>

- **Señal ploteada Ojos Abiertos y cerrados**

  <div align="center">
     <img src="../../Imagenes/Lab5/Figura_7.jpeg" height="300">
      <p>Figura 7. Señal ploteada con los ojos abiertos y cerrados durante 5 segundos cada fase
  </div>

- **Señal ploteada Basal 2**

  <div align="center">
     <img src="../../Imagenes/Lab5/Figura_8.jpeg" height="300">
      <p>Figura 8. Señal ploteada en estado de relajación como línea base segunda medición
  </div>

- **Señal ploteada Ejercicios Mentales**

  <div align="center">
     <img src="../../Imagenes/Lab5/Figura_9.jpeg" height="300">
      <p>Figura 9. Señal ploteada en estado de activación por ejercicios mentales de matemática
  </div>

### Ploteo de la señal en Python
En la parte de abajo se encuentran los códigos usados para adquirir estas señales por python, de la misma forma se entrega un único ejemplo de este. <br>
Código de ejemplo:
```python


```
#### Señal en Python Basal 1 (Bitalino)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_10.png" height="300">
    <p>Figura 10. Señal ploteada en estado de relajación como línea base primera medición en Python
</div>

#### Señal en Python Ojos Abiertos y cerrados (Bitalino)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_11.png" height="300">
    <p>Figura 11. Señal ploteada con los ojos abiertos y cerrados durante 5 segundos cada fase en Python
</div>

#### Señal en Python Basal 2 (Bitalino)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_12.png" height="300">
    <p>Figura 12. Señal ploteada en estado de relajación como línea base segunda medición en Python
</div>

#### Señal en Python Ejercicios Mentales (Bitalino)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_13.png" height="300">
    <p>Figura 13. Señal ploteada en estado de activación por ejercicios mentales de matemática en Python
</div>

#### Señal en Python Basal 1 (OpenBCI)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_14.png" height="300">
    <p>Figura 14. Señal ploteada en estado de relajación como línea base primera medición en Python con datos externos
</div>

#### Señal en Python Ojos Abiertos y cerrados (OpenBCI)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_15.png" height="300">
    <p>Figura 15. Señal ploteada con los ojos abiertos y cerrados durante 5 segundos cada fase en Python con datos externos
</div>

#### Señal en Python Basal 2 (OpenBCI)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_16.png" height="300">
    <p>Figura 16. Señal ploteada en estado de relajación como línea base segunda medición en Python con datos externos
</div>

#### Señal en Python Ejercicios Mentales (OpenBCI)

<div align="center">
   <img src="../../Imagenes/Lab5/Figura_17.png" height="300">
    <p>Figura 17. Señal ploteada en estado de activación por ejercicios mentales de matemáticas en Python con datos externos
</div>

### Archivos de las señales ploteadas 
- Aquí se presentan los archivos txt de la información para cada señal mostrada: <br>
   [Estado Basal 1](../../Documentacion/Laboratorios/Lab5)<br>
   [Ojos Abiertos - Cerrados](../../Documentacion/Laboratorios/Lab5)<br>
   [Estado Basal 2](../../Documentacion/Laboratorios/Lab5)<br>
   [Ejercicios mentales](../../Documentacion/Laboratorios/Lab5)

- Así mismo se muestran los archivos python que se usaron
Todos los códigos en:
[Códigos EEG .py](../../Software/Lab5)


## Discusión y conclusiones


## Referencias

[1] J. W. Britton, L. C. Frey, J. L. Hopp, et al., "Electroencephalography (EEG): An Introductory Text and Atlas of Normal and Abnormal Findings in Adults, Children, and Infants," St. Louis E. K., L. C. Frey, Eds. Chicago: American Epilepsy Society, 2016. [Online]. Available: [link](https://www.ncbi.nlm.nih.gov/books/NBK390354/)

[2] A. Rayi and N. Murr, "Electroencephalogram," StatPearls, updated Oct. 3, 2022. [Online]. Available: [link](https://www.ncbi.nlm.nih.gov/books/NBK563295/)

[3] BiTalino, Ed., Bitalino (r)evolution lab guide, [Online]. Available: [link](https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf). 

[4] Molina del Río, J., Guevara, M.A., Hernández González, M. et al. EEG correlation during the solving of simple and complex logical–mathematical problems. Cogn Affect Behav Neurosci 19, 1036–1046(2019). https://doi.org/10.3758/s13415-019-00703-5 
