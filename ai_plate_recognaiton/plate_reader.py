import cv2
import pytesseract
import os

# Função para procurar a imagem da placa
def find_image_path(image_name):
    # Caminhos típicos para procurar a imagem
    possible_paths = [
        os.path.join(os.getcwd(), 'imagens', image_name),
        os.path.join(os.path.dirname(__file__), 'imagens', image_name),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

# Carregar a imagem
image_name = 'test_plate.png'
image_path = find_image_path(image_name)

if image_path:
    print(f"[INFO] Imagem encontrada: {image_path}")
    image = cv2.imread(image_path)
else:
    print(f"[ERROR] O arquivo no caminho {image_name} não existe.")
    exit()

# Converter a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar limiarização para destacar as letras
# Aqui estamos utilizando um valor arbitrário de limiar 100 (ajuste conforme necessário)
_, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)

# Usar Tesseract OCR para detectar texto na imagem
custom_oem_psm_config = r'--oem 3 --psm 6'  # Usando OEM 3 (ambos LSTM e Tesseract) e PSM 6 (método de detecção de bloco de texto)
text = pytesseract.image_to_string(thresh_image, config=custom_oem_psm_config)

# Exibir o texto reconhecido
print(f"[INFO] Texto detectado: {text}")

# Salvar o texto em um arquivo .txt
output_file = 'placa_detectada.txt'
with open(output_file, 'w') as file:
    file.write(text)

print(f"[INFO] Texto salvo no arquivo {output_file}")

# Exibir a imagem com a limiarização aplicada
cv2.imshow("Imagem com Limiarização", thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
