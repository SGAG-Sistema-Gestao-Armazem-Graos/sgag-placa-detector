import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import datetime

# Cria a pasta para salvar as imagens
SAVE_DIR = "leitura_placa\imagens_caminhao"
os.makedirs(SAVE_DIR, exist_ok=True)

# Função para tirar foto com a webcam
def tirar_foto():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a webcam.")
        return

    ret, frame = cap.read()
    cap.release()
    if ret:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"caminhao_{timestamp}.jpg"
        path = os.path.join(SAVE_DIR, filename)
        cv2.imwrite(path, frame)
        messagebox.showinfo("Foto capturada", f"Imagem salva como: {path}")
    else:
        messagebox.showerror("Erro", "Não foi possível capturar a imagem.")

# Função para upload de imagem
def fazer_upload():
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Arquivos JPG", "*.jpg"), ("Todos os arquivos", "*.*")]
    )
    if file_path:
        try:
            filename = os.path.basename(file_path)
            new_path = os.path.join(SAVE_DIR, f"upload_{filename}")
            with open(file_path, 'rb') as src, open(new_path, 'wb') as dst:
                dst.write(src.read())
            messagebox.showinfo("Upload", f"Imagem copiada para: {new_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao copiar imagem: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Captura de Caminhões")

btn_foto = tk.Button(root, text="Tirar Foto", command=tirar_foto, width=25, height=2)
btn_upload = tk.Button(root, text="Fazer Upload", command=fazer_upload, width=25, height=2)

btn_foto.pack(pady=10)
btn_upload.pack(pady=10)

root.mainloop()
