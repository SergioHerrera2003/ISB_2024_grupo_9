# LABORATORIO Nº 7 - TRANSFORMADA WAVELET

## Introducción
La transformada wavelet (WT) se ha establecido como la solución más avanzada para las limitaciones de la transformada de Fourier. Las funciones wavelet están localizadas tanto en el espacio como en los dominios de frecuencia y suelen representar la escala de tiempo. En el ámbito de las señales biomédicas, la mayoría de las características estadísticas no son estacionarias [1].

La transformada wavelet ofrece un método alternativo para analizar señales biomédicas no estacionarias, proporcionando una resolución de tiempo-frecuencia variable en el plano tiempo-frecuencia [2]. Esta técnica descompone una señal biomédica en bandas de frecuencia que están localizadas en el tiempo y la frecuencia. A bajas frecuencias, el tamaño de la ventana es grande para detectar cambios abruptos, mientras que a altas frecuencias, el tamaño de la ventana es pequeño. La capacidad de localización de la transformada wavelet permite aislar singularidades y estructuras irregulares en la señal. Además, la transformada wavelet requiere menos espacio de almacenamiento en comparación con otros métodos de análisis de tiempo-frecuencia. En esta transformada, el tamaño y las dimensiones de la salida son casi iguales a las de la entrada, lo que es una característica ventajosa en el procesamiento de imágenes de señales biomédicas. La transformada wavelet se ha convertido en una técnica muy poderosa y reconocida en la detección de características, reducción de ruido y compresión de señales en el procesamiento de imágenes. [3]


## Objetivos
- Implementar la DWT en señales biomédicas
- Evaluar la efectividad de la DWT en la reducción de ruido
- Aprender a usar la transformada Wavelet en aplicaciones biomédicas usando correctamente los parámetros necesarios

## Metodología
En base a los dataset recopilados en los anteriores laboratorios: EMG, ECG y EEG, se aplicarán DWT  para mejorar la calidad de las señales biomédicas. la presentación de los resultados se dará en una tabla, seguido de la documentación en el repositorio GitHub.

### Para señales EMG:
- **Preprocesamiento:**
    - Según el paper buscado en la literatura de la clasificación de EMG usando DWT [sergio1], este se basó en el movimiento de la mano. En nuestro caso, nos enfocaremos en el brazo, sin embargo, las recomendaciones de este paper son en base a los movimientos tanto de muñeca como dedos, así que hay que tomarlo como consideración.

    - La señal EMG inicial se filtra usando un filtro pasa banda en el rango de 5-160 Hz para eliminar el ruido y otras señales no deseadas. Esta etapa es crucial para mejorar la calidad de la señal y asegurar que los datos sean aptos para análisis posteriores. [sergio1]

- **Transformada Wavelet Discreta (DWT):**

    - Se elige una wavelet madre adecuada para descomponer la señal EMG. En este caso, se utiliza la wavelet Daubechies db3, conocida por su capacidad para capturar características relevantes en señales biomédicas. [sergio1]

- **Descomposición de la señal:**

    - La señal EMG se pasa a través de filtros pasa alto y pasa bajo secuencialmente para obtener coeficientes de detalle y aproximación en cada nivel de descomposición. Esto se repite hasta alcanzar el nivel deseado de descomposición. Para el análisis en el documento, se establece un nivel de descomposición de hasta 8, generando subconjuntos de coeficientes de detalle (cd1, cd2, cd3, cd4, cd5, cd6, cd7, cd8) y un coeficiente de aproximación. [sergio1]
    - Para el umbral, nos basamos en una fórmula que también se realiza en otros papers para la Transformada de Wavelet [sergio2]. Así pues nos deja completar el cálculo para efectuar este filtro a la señal original.

    <div align="center">
    <img src="../../Imagenes/Lab7/Ecuacion_1.jpeg" height="150">
        <p>Figura 1. Ecuación para el Umbral
    </div>

### Para señales ECG:
- **Filtrado con Wavelet tipo db4:**
  - Se recomienda utilizar una wavelet tipo db4 para eliminar los componentes de alta frecuencia de la señal.
  - Se utilizan 8 niveles de descomposición para asegurar una eliminación efectiva de las frecuencias no deseadas.
  - Se aplica una ventana de 5 segundos para el procesamiento de la señal en cada nivel de descomposición.
  - Posteriormente, se realiza un filtrado de media móvil para eliminar los ruidos de bajas frecuencias y suavizar la señal.


### Para señales EEG:

- **Filtro Pasabanda IIR Butterworth:** 
    - Se recomienda en la bibliografía un filtro pasabanda IIR Butterworth con frecuencia de corte de 0.5 Hz a 35 Hz para eliminar el ruido no deseado de la señal.
    
- **Ventana de señal:** 
    - Se utilizó una ventana de 21 s para el procesamiento de la señal, según las recomendaciones de la bibliografía.

- **Tipo de Wavelet:** 
    - Se utilizó la wavelet madre "db4" según la bibliografía, que es conocida por sus propiedades útiles en el procesamiento de señales biomédicas.

- **Número de niveles de descomposición:**
    - La señal se dividió en 5 niveles de descomposición, según las recomendaciones de la bibliografía.
## Resultados
### Tabla EMG:
| Campo              | Señal Cruda             | Señal filtrada con DWT       |
|--------------------|-------------------------|-------------------------------|
| Descanso - Basal  | <img src="../../Imagenes/Lab7/EMG_Basal.jpeg" height="200"> | <img src="../../Imagenes/Lab7/EMG_Basal_DWT.jpeg" height="200"> |
| Contracción débil | <img src="../../Imagenes/Lab7/EMG_Movimiento.jpeg" height="200"> | <img src="../../Imagenes/Lab7/EMG_Movimiento_DWT.jpeg" height="200"> |
| Contracción fuerte| <img src="../../Imagenes/Lab7/EMG_Oposicion.jpeg" height="200"> | <img src="../../Imagenes/Lab7/EMG_Oposicion_DWT.jpeg" height="200"> |

#### Códigos
- [Descanso - Basal](../../Software/Lab7/Brazo_basal.ipynb)
- [Contracción débil](../../Software/Lab7/Brazo_movimiento.ipynb)
- [Contracción fuerte](../../Software/Lab7/Brazo_oposicion.ipynb)

### Tabla ECG:
| Campo              | Señal Cruda             | Señal filtrada con DWT       |
|--------------------|-------------------------|-------------------------------|
| Descanso - Basal  | <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |
| Post Ejercicio | <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |
| Recuperación| <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |

#### Códigos
- [Basal](../../Software/Lab7)
- [Post Ejercicio](../../Software/Lab7)
- [Recuperación](../../Software/Lab7)

### Tabla EEG:
| Campo              | Señal Cruda             | Señal filtrada con DWT       |
|--------------------|-------------------------|-------------------------------|
| Basal  | <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |
| Ojos abiertos - cerrados | <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |
| Ejercicios Mentales| <img src="../../Imagenes/Lab7" height="200"> | <img src="../../Imagenes/Lab7" height="200"> |


#### Códigos
- [Basal](../../Software/Lab7)
- [Ojos abierto - cerrados](../../Software/Lab7)
- [Ejercicios Mentales](../../Software/Lab7)

## Discusión y Conclusiones

### Para Señales EMG:
La aplicación de la Transformada Wavelet Discreta (DWT) en el análisis del reposo del brazo revela la capacidad de filtrar esta señal por sus coeficientes. Así se puede identificar patrones y tendencias tanto en el dominio del tiempo como en el de la frecuencia, lo que resulta útil para entender la actividad muscular en reposo. Se observa que durante el reposo del brazo, las componentes de baja frecuencia son predominantes, mientras que las de alta frecuencia contribuyen mínimamente a la información relevante de la señal.

Al aplicar la DWT al análisis del movimiento del brazo, se destaca su capacidad para discernir entre los diferentes niveles de esfuerzo muscular que realiza. La descomposición en coeficientes de detalle y aproximación permite capturar las características globales de la señal como los detalles finos relacionados con la fuerza y la dirección del movimiento. Se observan movimientos en la amplitud más grandes que en reposo.

En el caso del movimiento de oposición del brazo con mayor fuerza, la aplicación de la DWT revela cambios significativos en las características de la señal sEMG en comparación con otros movimientos, existen ondas más pronunciadas y resaltan más otros tipos de onda que en los que se presentan únicamente los de movimiento o reposo.

En general, basado en los resultados obtenidos, se evidencia que el proceso de descomposición de la señal mediante la DWT proporciona información detallada sobre la actividad muscular durante diferentes tipos de movimientos del brazo. La capacidad de la DWT para identificar patrones y tendencias en las señales sEMG puede ser de gran utilidad en aplicaciones de rehabilitación y control de prótesis. [sergio1].

En conclusión, este laboratorio nos enseñó a destacar el potencial de la DWT como una herramienta de análisis de señales sEMG para aplicaciones de movimiento del brazo.
### Para Señales ECG:
En ingeniería biomédica, el electrocardiograma (ECG) es una herramienta crucial para monitorear las señales del corazón [guille1]. Sin embargo, las señales de ECG a menudo contienen ruido, lo que complica su análisis. La transformada wavelet es una herramienta para procesamiento de señales biomédicas, debido a que proporciona información tanto en el dominio del tiempo como en el de la frecuencia, por lo que es ideal para analizar señales no estacionarias como el ECG. La transformada wavelet se utiliza para reducir el ruido en las señales de ECG y mejorar la detección de eventos cardíacos clave como los complejos QRS, las ondas P y las ondas T [guille2].

Se observa que, con la aplicación de la transformada wavelet, las señales de ECG mejoraron en la claridad de la señal. Al seleccionar funciones wavelet y niveles de descomposición de acuerdo a [guille3], aislamos y eliminamos el ruido mientras preservábamos las características cardíacas esenciales. Esto mejoró la visibilidad de los complejos QRS, las ondas P y las ondas T, facilitando una interpretación más precisa. Comparando con el resultado obtenido en con el método aplicado anteriormente en laboratorio de filtros FIR e IR, se obtuvieron mejores resultados.

Además, el enfoque basado en wavelets mejora la relación señal-ruido, este método podría aumentar la precisión de los sistemas de análisis automático de ECG, llevando a mejores resultados diagnósticos [guille4]. Los resultados apoyan el uso y desarrollo continuado de técnicas wavelet en el procesamiento de señales biomédicas, especialmente para aplicaciones que requieren un análisis temporal y espectral preciso.
### Para Señales EEG:

## Bibliografía

[1]. Y. Attikiouzel, ‘Biomedical signal processing: present and future’, Proceedings of the 5th International Symposium on Signal Processing and Its Applications, ISSPA’99, vol. 1, 1999.
[2]. I. Daubechies, ‘Orthonormal bases of compactly supported wavelets’, Communications on Pure and Applied Mathematics, vol. 41, no. 7, pp. 909–996, 1988.
[3]. F. Abramovich, T. C. Bailey, and T. Sapatinas, ‘Wavelet analysis and its statistical applications’, Journal of the Royal Statistical Society: Series D (The Statistician), vol. 49, no. 1, pp. 1–29, 2000.

[sergio1] Aljebory, Karim & Jwmah, Yashar & Mohammed, Thabit. (2024). Classification of EMG Signals Using DWT Features and ANN Classifier. 51. 23-32. [PDF](https://www.iaeng.org/IJCS/issues_v51/issue_1/IJCS_51_1_04.pdf) 

[sergio2] M. Boyer, L. Bouyer, J.-S. Roy, and A. Campeau-Lecours, “Reducing noise, artifacts and Interference in Single-Channel EMG Signals: a review,” Sensors, vol. 23, no. 6, p. 2927, Mar. 2023, [doi: 10.3390/s23062927](https://doi.org/10.3390/s23062927).

[guille1] Selcan Kaplan Berkaya, et al. "A survey on ECG analysis," Biomedical Signal Processing and Control, vol. 43, pp. 216-235, 2018.

[guille2] S. Goel, P. Tomar, and G. Kaur, "An optimal wavelet approach for ECG noise cancellation," International Journal of Bio-Science and Bio-Technology, vol. 8, no. 4, pp. 39-52, 2016.

[guille3] P. M. Shemi and E. M. Shareena, "Analysis of ECG signal denoising using discrete wavelet transform," in 2016 IEEE International Conference on Engineering and Technology (ICETECH), Coimbatore, India, 2016, pp. 713-718.

[guille4] M. E. Alexander, R. Baumgartner, A. R. Summers, C. Windischberger, M. Klarhoefer, E. Moser, and R. L. Somorjai, "A wavelet-based method for improving signal-to-noise ratio and contrast in MR images," Magnetic Resonance Imaging, vol. 18, no. 2, pp. 169-180, 2000, doi: 10.1016/S0730-725X(99)00128-9. [Online]. Available: [https://www.sciencedirect.com/science/article/pii/S0730725X99001289](https://www.sciencedirect.com/science/article/pii/S0730725X99001289)
