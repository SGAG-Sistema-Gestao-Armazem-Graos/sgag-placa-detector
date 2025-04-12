# plate_reader.py

import easyocr
import cv2

def read_plate(image):
    """
    Função que utiliza OCR (EasyOCR) para reconhecer e extrair o texto de uma placa de veículo.

    :param image: Imagem que contém a placa (np.ndarray).
    :return: Texto extraído da placa.
    """
    # Inicializa o leitor OCR
    reader = easyocr.Reader(["pt"])

    # Aplica OCR na imagem
    result = reader.readtext(image)

    # Se houver resultado
    if result:
        # Extrai o texto da primeira placa detectada
        plate_text = result[0][1]
        return plate_text
    else:
        return "Placa não detectada"

# Teste rápido
if __name__ == "__main__":
    # Carregar uma imagem de teste
    image_path = 'images/test_plate.jpg'  # Caminho para a imagem
    image = cv2.imread(image_path)

    if image is not None:
        # Tenta ler a placa
        plate = read_plate(image)
        print(f"Texto extraído da placa: {plate}")
    else:
        print("Falha ao carregar a imagem.")
