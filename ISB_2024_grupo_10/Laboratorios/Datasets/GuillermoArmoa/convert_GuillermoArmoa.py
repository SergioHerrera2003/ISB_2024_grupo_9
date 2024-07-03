import pandas as pd

# Leer el archivo de texto ignorando las líneas de metadata
with open('EMG_data/Brazo_reposo-2.txt', 'r') as file:
    lines = file.readlines()

# Ignorar líneas de metadata
data_lines = [line for line in lines if not line.startswith('#')]

# Crear una lista con los nombres de las columnas
Fs = 1000 # Hz
Ts = 1/Fs # Segundos
ts = 1 # ms

# Crear una lista con los nombres de las columnas
column_names = [f'sig{i}' for i in range(len(data_lines[0].split()))]

# Crear un DataFrame a partir de los datos
data = [line.strip().split() for line in data_lines]
df = pd.DataFrame(data, columns=column_names)

# Añadir la columna timestamp
df.insert(0, 'timestamp', range(len(df)))

# Guardar el DataFrame en un archivo CSV
df.to_csv('EMG_data/EMG.brazo_reposo.csv', index=False)
