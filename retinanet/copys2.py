import os
import pandas as pd

# Directorios principales
base_dirs = ['cloudy', 'shaded', 'sunny']
annotations_file = os.path.join('test', '_annotations.csv')

# Leer el archivo de anotaciones
if not os.path.exists(annotations_file):
    print(f"No se encontró el archivo {annotations_file}.")
else:
    annotations_df = pd.read_csv(annotations_file, header=None, names=['filename', 'x_min', 'y_min', 'x_max', 'y_max', 'label'])

    # Iterar sobre las carpetas base
    for base in base_dirs:
        images_dir = os.path.join(base, 'images')
        output_csv = os.path.join(images_dir, '_annotations.csv')

        # Listar los nombres de archivos en la carpeta de imágenes (sin extensión)
        image_files = {os.path.splitext(f)[0] for f in os.listdir(images_dir)}

        # Filtrar las anotaciones que coincidan con los archivos de imágenes
        matching_annotations = annotations_df[
            annotations_df['filename'].apply(lambda x: os.path.splitext(x)[0]).isin(image_files)
        ]

        # Eliminar las líneas coincidentes del DataFrame original
        annotations_df = annotations_df.drop(matching_annotations.index)

        # Crear el archivo _annotations.csv si hay coincidencias
        if not matching_annotations.empty:
            matching_annotations.to_csv(output_csv, index=False, header=False)
            print(f"Archivo creado: {output_csv}")
        else:
            print(f"No se encontraron coincidencias para {base}.")

    # Sobrescribir el archivo original con las líneas restantes
    annotations_df.to_csv(annotations_file, index=False, header=False)
    print(f"Archivo original actualizado: {annotations_file}")
