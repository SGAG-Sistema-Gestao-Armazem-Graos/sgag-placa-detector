from camera import capture_image
from plate_reader import read_plate_text

def detect_plate():
    image = capture_image()
    if image is not None:
        plate_text = read_plate_text(image)
        print(f"Placa detectada: {plate_text}")
    else:
        print("Erro ao capturar imagem.")
