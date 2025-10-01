import cv2
import os

def video_to_frames(video_path, output_folder,color):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Capturar el video
    cap = cv2.VideoCapture(video_path)
    count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Guardar cada frame como una imagen
        frame_path = os.path.join(output_folder, f'frame{color}_{count:05d}.jpg')
        cv2.imwrite(frame_path, frame)
        count += 1
    
    cap.release()
    print(f'Total de frames extraídos: {count}')

# Uso de la función
color="negro" #Colocar Nombre del color
video_path = f'{color}.mp4'
output_folder = f'dataset/{color}'
video_to_frames(video_path, output_folder,color)