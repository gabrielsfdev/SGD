from tkinter import filedialog, PhotoImage 
from baseApp import BaseApp

class Photo(BaseApp):
    def upload_image(self):
        global image, image_id  # Declara as variáveis image e image_id como globais
        filename = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Arquivos de Imagem", "*.jpg *.png")])  # Abre uma janela de diálogo para selecionar um arquivo de imagem
        if filename:  # Verifica se o usuário selecionou um arquivo
            image = PhotoImage(file=filename)  # Carrega a imagem selecionada
            image_id = self.canvas.create_image(512, 124, anchor="center", image=image)  # Cria a imagem no canto superior esquerdo do Canvas
            self.canvas.bind("<Button-1>", self.start_move)  # Liga o evento de pressionar o botão esquerdo do mouse
            self.canvas.bind("<B1-Motion>", self.on_move)    # Liga o evento de mover o mouse enquanto o botão esquerdo do mouse está pressionado
            self.canvas.bind("<ButtonRelease-1>", self.end_move)  # Liga o evento de soltar o botão esquerdo do mouse

    def start_move(self, event):
        global start_x, start_y  # Declara as variáveis start_x e start_y como globais
        start_x = event.x  # Armazena a posição x do mouse quando o botão é pressionado
        start_y = event.y  # Armazena a posição y do mouse quando o botão é pressionado

    def on_move(self, event):
        global start_x, start_y, image_id  # Declara as variáveis start_x, start_y e image_id como globais
        dx = event.x - start_x  # Calcula a diferença entre a posição atual do mouse e a posição inicial do mouse em x
        dy = event.y - start_y  # Calcula a diferença entre a posição atual do mouse e a posição inicial do mouse em y
        self.canvas.move(image_id, dx, dy)  # Move a imagem na tela de acordo com a diferença calculada
        start_x = event.x  # Atualiza a posição inicial do mouse em x
        start_y = event.y  # Atualiza a posição inicial do mouse em y

    def end_move(event):
        pass  # Não é necessário fazer nada quando o botão do mouse é solto