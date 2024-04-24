from tkinter import filedialog, PhotoImage 
from baseApp import BaseApp
import cv2
import os
import tempfile

class Photo(BaseApp):
    def upload_image(self):
        global image, image_id  # Declara as variáveis image e image_id como globais
        filename = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Arquivos de Imagem", "*.jpg *.png")])  # Abre uma janela de diálogo para selecionar um arquivo de imagem
        print(filename)

        if filename:  # Verifica se o usuário selecionou um arquivo
            # Abre a imagem usando OpenCV
            img = cv2.imread(filename)
            if img is None:
                print("Erro ao carregar o arquivo de imagem.")
                return

            # Redimensiona a imagem para o tamanho desejado
            img = cv2.resize(img, (190, 130))  # Altere 300 e 200 para o tamanho desejado

            # Salva temporariamente a imagem em um arquivo
            temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
            cv2.imwrite(temp_file.name, img)

            # Cria o PhotoImage usando o arquivo temporário
            image = PhotoImage(file=temp_file.name)

            # Remove o arquivo temporário
            temp_file.close()
            os.unlink(temp_file.name)

            # Cria a imagem no canto superior esquerdo do Canvas
            image_id = self.canvas.create_image(512, 124, anchor="center", image=image)