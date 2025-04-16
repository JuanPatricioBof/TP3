import pathlib
import csv
import os
def unir_archivos_individuos(ruta_entrada, archivo_salida):
    # Filtrar archivos de forma robusta solo para los que empiezan con 'usu_individual' y terminan con '.txt'
    archivos = [
        f for f in os.listdir(ruta_entrada)
        if f.startswith('usu_individual') and f.endswith('.txt')
    ]

    # Ordenar los archivos por nombre para asegurarse de que se procesen en el orden correcto
    archivos.sort()

    # Lista para almacenar las filas de todos los archivos
    filas_totales = []
    
    # Variable para almacenar el encabezado
    encabezado = None

    # Leer cada archivo de la lista de archivos
    for nombre_archivo in archivos:
        # Suponiendo que ya tienes ruta_entrada como Path, y nombre_archivo como el nombre del archivo
        archivo_path = ruta_entrada / nombre_archivo
        # Abrir cada archivo en modo lectura
        with open(archivo_path, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=';')

            # Usamos next() sin un condicional explícito para manejar el encabezado
            if encabezado is None:
                encabezado = next(lector)  # Asignamos el encabezado del primer archivo
            else:
                next(lector)  # Saltamos el encabezado de los archivos subsiguientes

            # Agregar las filas leídas del archivo actual a la lista total
            filas_totales.extend(lector)

    # Escribir los resultados combinados en el archivo de salida dentro de 'files'
    with open(archivo_salida, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=',')
        
        # Escribir el encabezado una sola vez
        escritor.writerow(encabezado)
        
        # Escribir las filas combinadas
        escritor.writerows(filas_totales)