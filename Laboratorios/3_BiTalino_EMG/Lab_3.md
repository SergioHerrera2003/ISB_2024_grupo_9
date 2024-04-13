# LABORATORIO 3: Uso de BiTalino para EMG

## Tabla de contenidos
1. [Objetivos](#objetivos)
2. [Materiales y equipos](#materiales-y-equipos)
3. [Procedimiento](#procedimiento)
4. [Resultados](#resultados)
   - 3.1 [Conexión usada](#31-conexión-usada)
   - 3.2 [Video de la señal y ploteo de la señal en OpenSignal](#32-video-de-la-señal-y-ploteo-de-la-señal-en-opensignal)
   - 3.3 [Resumen](#33-resumen)
   - 3.4 [Archivos](#34-archivos)
   - 3.5 [Ploteo de la señal en Python](#35-ploteo-de-la-señal-en-python)

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
- Instalar OpenSignals (r)evolution: [Descarga aquí](https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-boardkit-ble-bt)
- Descargar la versión de 64 bits.
### 3.2 Conexión del BITalino con OpenSignals
1. Activar el Bluetooth para configurar la tarjeta BITalino.
2. Conectar la batería a la placa BITalino.
3. Encender la placa.
4. Buscar la tarjeta BITalino.
5. Agregar el pin “1234” que se muestra en la guía de inicio rápido.
6. Una vez listo, aparecerá de color azul la opción Enable en OpenSignals, lo que indica que el BITalino está listo para usarse.
7. Conectar los cables a A1, que es el puerto para Electromiografía (EMG).
8. Colocar los electrodos en los cables y posicionarlos en el lugar de la medición.

### 3.2 Posicionamiento de los electrodos
- Se emplearon las posiciones referentes de electromiografía otorgadas por la guía para realizar la colocación de electrodos en el bíceps y en los músculos tenares ubicados debajo del pulgar.

## Resultados
### 4.1 Posicionamiento 1: Biceps
- Fotos conexión usada.
- Video de señal en silencio eléctrico o reposo.
- Video de señal en flexión y extensión.
- Video de señal con fuerza de oposición.
- Ploteo de cada señal.

### 4.1 Posicionamiento 2: Pulgar
- Fotos conexión usada.
- Video de señal en silencio eléctrico o reposo + ploteo en OpenSignal.
- Video de señal en flexión y extensión.
- Video de señal con fuerza de oposición.
- Video de guerra de pulgares.
- Ploteo de cada señal (Python).

### Ploteo de la señal del dedo gordo en reposo

### 4.3  Resumen
En el laboratorio de Introducción a Señales Biomédicas, se realizó la medición de la actividad muscular mediante un electromiógrafo con electrodos superficiales. Se identificó una correlación positiva entre la fuerza muscular y el voltaje registrado, evidenciando un aumento proporcional en el voltaje conforme aumentaba la fuerza muscular. Durante el estudio, se efectuaron tres tomas de señal: en reposo, durante movimientos leves y al aplicar resistencia. En las gráficas resultantes, se observaron distintos patrones de actividad muscular: en reposo se identificó una línea de base estable, durante movimientos leves se registró un incremento correspondiente a la actividad muscular del movimiento ejecutado, y al aplicar resistencia se evidenció una mayor actividad muscular, reflejada en picos más pronunciados y una amplitud mayor. Además, se mostró la colocación de los electrodos del EMG en el músculo abductor pollicis brevis y el bíceps, permitiendo visualizar el estado relajado y la contracción muscular en distintas condiciones.
