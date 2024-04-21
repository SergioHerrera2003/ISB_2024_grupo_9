# LABORATORIO 3: Uso de BiTalino y Adquisición de Señales EMG


## Tabla de contenidos
1. [Objetivos](#objetivos)
2. [Materiales y equipos](#materiales-y-equipos)
3. [Procedimiento](#procedimiento)
4. [Entregables](#entregables)
   - 4.1 [Señales del Biceps](#41-posicionamiento-1-biceps)
   - 4.2 [Señales del Dedo Pulgar](#42-posicionamiento-2-pulgar)

## Objetivos
- Adquirir señales biomédicas de EMG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution.

## Materiales y equipos
| MODELO | DESCRIPCIÓN               | CANTIDAD |
|--------|---------------------------|----------|
| ( R ) EVOLUTION | Kit BITalino     | 1        |
|        | Laptop o PC               | 1        |

## Procedimiento
### 3.1 Instalación de OpenSignals
- Instalar OpenSignals (R)evolution: [Descarga aquí](https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-boardkit-ble-bt)
- Descargar la versión de 64 bits.
### 3.2 Conexión del BITalino con OpenSignals
1. Activar el Bluetooth para configurar la tarjeta BITalino.
2. Conectar la batería a la placa BITalino.
3. Encender la placa.

   <div align="center">
    <img src="../../Imagenes/Lab3/Figura1.jpeg" width="200" height="300">
    <p>Fig 1. Manual de BiTalino

4. Buscar la tarjeta BITalino.
   <div align="center">
    <img src="../../Imagenes/Lab3/Figura2.jpeg" width="400" height="200">
      <p>Fig 2. Pantalla de Inicio OpenSignals
<br>

5. Agregar el pin “1234” que se muestra en la guía de inicio rápido.

6. Una vez listo, aparecerá de color azul la opción Enable en OpenSignals, lo que indica que el BITalino está listo para usarse.

7. Conectar los cables a A1, que es el puerto para Electromiografía (EMG). 
   <div align="center">
    <img src="../../Imagenes/Lab3/Figura3.jpeg" width="400" height="200">
      <p>Fig 3. Canales del BiTalinmos. Canal A1
<br>

8. Colocar los electrodos en los cables y posicionarlos en el lugar de la medición.

### 3.2 Posicionamiento de los electrodos
- Se emplearon las posiciones referentes de electromiografía otorgadas por la guía para realizar la colocación de electrodos en el bíceps y en los músculos tenares ubicados debajo del pulgar.

## Entregables
### 4.1 Señal de Biceps
- Fotos conexión usada (Electrodos,cuerpo y bitalino).
   <div align="center">
    <img src="../../Imagenes/Lab3/BicepReposo.jpeg" width="400" height="400">
   <p>Fig 4. Conexiones del bícep
<br>

- Videos (Clik para visualizar):
   - Video de señal en silencio eléctrico o reposo. <br>
   <a href="https://www.youtube.com/watch?v=X4ClBcfxJsI">
    <img src="https://img.youtube.com/vi/X4ClBcfxJsI/mqdefault.jpg" width="400" height="225">
  </a> 
  <br>
   - Video de señal en flexión y extensión.
   <br>
   <a href="https://www.youtube.com/watch?v=fOo3VtrS6gE">
    <img src="https://img.youtube.com/vi/fOo3VtrS6gE/mqdefault.jpg" width="400" height="225">
  </a>
  <br>
   - Video de señal con fuerza de oposición.
   <br>
   <a href="https://www.youtube.com/watch?v=ctoRjxKaLMY">
    <img src="https://img.youtube.com/vi/ctoRjxKaLMY/mqdefault.jpg" width="400" height="225">
  </a>

- Ploteo en OpenSignals.
   <br>
      <div align="center">
    <img src="../../Imagenes/Lab3/ReposoBrazo.jpeg" width="400" height="200">
      <p> Fig 5. Señal en Reposo de Brazo
   <br>
   <div align="center">
    <img src="../../Imagenes/Lab3/MovimientoBrazo.jpeg" width="400" height="200">
      <p> Fig 6. Señal en Flexión y extensión de Brazo
   <br>
   <div align="center">
    <img src="../../Imagenes/Lab3/OposicionBrazo.jpeg" width="400" height="200">
      <p> Fig 7. Señal en Oposición de Brazo
   <br>

- Archivos de los datos de las señales <br>
   Descargar Brazo Reposo:    [Documento Reposo Brazo](../../Documentacion/Laboratorios/Lab3/Brazo_reposo.txt)
   <br>
   Descargar Brazo Flexión:   [Documento Movimiento Brazo](../../Documentacion/Laboratorios/Lab3/brazo_movimiento.txt)
   <br>
   Descargar Brazo Oposición: [Documento Oposición Brazo](../../Documentacion/Laboratorios/Lab3/brazo_oposicion.txt)
- Ploteo cada señal en (Python)

<div align="center">
  <img src="../../Imagenes/Lab3/SeñalBicepReposo5s.png" width="300">
  <p>Fig 8. Ploteo en Python Bícep Reposo <br>

  <img src="../../Imagenes/Lab3/SeñalBicepsFlexionExtension15s.png" width="300">
  <p>Fig 9. Ploteo en Python Bícep Flexión y extensión <br>

  <img src="../../Imagenes/Lab3/SeñalDedoPulgarOposición.png" width="300">
  <p>Fig 10. Ploteo en Python Bícep Oposición
</div>

### 4.2 Señal de Pulgar
- Fotos conexión usada.
   <div align="center">
    <img src="../../Imagenes/Lab3/PulgarElectrodo.jpeg" width="400" height="250">
   <p>Fig 11. Conexiones del pulgar
<br>

- Videos (Clik para visualizar):
   - Video de señal en silencio eléctrico o reposo
   <a href="https://www.youtube.com/watch?v=yWJ9BlEAWvw">
    <img src="https://img.youtube.com/vi/yWJ9BlEAWvw/mqdefault.jpg" width="400" height="225">
   </a>
   <br>
   - Video de señal en flexión y extensión.
   <br>
    <a href="https://www.youtube.com/watch?v=j-K2yEnZCDM">
    <img src="https://img.youtube.com/vi/j-K2yEnZCDM/mqdefault.jpg" width="400" height="225">
   </a>
   <br>
   - Video de señal con fuerza de oposición.
   <br>
   <a href="https://www.youtube.com/watch?v=VwWszo3aDsk">
    <img src="https://img.youtube.com/vi/VwWszo3aDsk/mqdefault.jpg" width="400" height="225">
   </a>

- Ploteo en OpenSignals.
   <br>
      <div align="center">
    <img src="../../Imagenes/Lab3/ReposoPulgar.jpeg" width="400" height="200">
      <p> Fig 12. Señal en Reposo de Pulgar
   <br>
   <div align="center">
    <img src="../../Imagenes/Lab3/MovimientoPulgar.jpeg" width="400" height="200">
      <p> Fig 13. Señal en Flexión y extensión de Pulgar
   <br>
   <div align="center">
    <img src="../../Imagenes/Lab3/OposicionPulgar.jpeg" width="400" height="200">
      <p> Fig 14. Señal en Oposición de Pulgar
   <br>

- Archivos de los datos de las señales

   Descargar Pulgar Reposo:    [Documento Reposo Pulgar](../../Documentacion/Laboratorios/Lab3/reposo_pulgar.txt)
   <br>
   Descargar Pulgar Flexión:   [Documento Movimiento Pulgar](../../Documentacion/Laboratorios/Lab3/pulgar.txt)
   <br>
   Descargar Pulgar Oposición: [Documento Oposición Pulgar](../../Documentacion/Laboratorios/Lab3/oposicion_pulgar.txt)

- Ploteo de cada señal (Python).
<div align="center">
  <img src="../../Imagenes/Lab3/SeñalPulgarReposo.png" width="300">
  <p>Fig 15. Ploteo en Python Pulgar Reposo <br>

  <img src="../../Imagenes/Lab3/SeñalDedoGordo.png" width="300">
  <p>Fig 16. Ploteo en Python Pulgar Flexión y extensión <br>

  <img src="../../Imagenes/Lab3/SeñalDedoPulgarOposición.png" width="300">
  <p>Fig 17. Ploteo en Python Pulgar Oposición
</div>



### Ploteo de la señal del dedo gordo en reposo

### 4.3 Resumen Laboratorio y Discusión

En el laboratorio de Introducción a Señales Biomédicas, se llevó a cabo la medición de la actividad muscular mediante un electromiógrafo equipado con electrodos superficiales. Durante el laboratorio, se identificó una correlación
positiva entre la fuerza muscular y el voltaje registrado, lo que evidenció un aumento proporcional en el voltaje conforme aumentaba la fuerza muscular. Se mostró la colocación de los electrodos del EMG en el músculo abductor pollicis brevis y el bíceps, permitiendo visualizar tanto el estado relajado como la contracción muscular en distintas condiciones.

Se realizaron tres tomas de señal distintas: una en reposo, otra durante movimientos leves y la última al aplicar resistencia. En las gráficas resultantes, se observaron distintos patrones de actividad muscular:

   - En la toma de señal en reposo, se identificó una línea de base estable, reflejando el estado de inactividad muscular.
   - Durante los movimientos leves, se registró un incremento, indicando una respuesta fisiológica acorde al esfuerzo realizado.
   - Al aplicar resistencia, se evidenció una mayor actividad muscular, manifestada en picos más pronunciados y una amplitud mayor en la señal registrada. Esto sugiere una respuesta muscular más intensa ante la demanda de fuerza externa.

### Referencias Bibliográficas
[1]Bbk, “BITalino (r)evolution Board Kit Data Sheet.”
<br>
[2] “BITalino (r)evolution User Manual BITalino (r)evolution User Manual.”