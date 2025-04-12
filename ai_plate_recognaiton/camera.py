import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None
    
    print("Pressione 's' para capturar a imagem.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Captura de Placa", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_path = "images/captured_plate.jpg"
            cv2.imwrite(img_path, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return img_path
