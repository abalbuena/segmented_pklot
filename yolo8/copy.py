import os
import shutil

# Directorios principales
base_dirs = ['cloudy', 'shaded', 'sunny']
labels_dir = 'labels'

# Iterar sobre las carpetas base
for base in base_dirs:
    images_dir = os.path.join(base, 'images')
    labels_subdir = os.path.join(base, 'labels')
    
    # Crear la subcarpeta de labels si no existe
    os.makedirs(labels_subdir, exist_ok=True)

    # Listar los archivos en la carpeta de imágenes y labels
    image_files = [os.path.splitext(f)[0] for f in os.listdir(images_dir)]
    label_files = os.listdir(labels_dir)

    # Mover los archivos de labels que coincidan con las imágenes
    for label_file in label_files:
        label_name, label_ext = os.path.splitext(label_file)
        if label_name in image_files:
            src_path = os.path.join(labels_dir, label_file)
            dest_path = os.path.join(labels_subdir, label_file)
            shutil.move(src_path, dest_path)
            print(f'Movido: {src_path} -> {dest_path}')
