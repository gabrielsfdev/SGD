from tkinter import Canvas, PhotoImage, Button
from baseApp import BaseApp
import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from app.services import Mascara

class BaseTab(BaseApp):
    def create_canvas_in_tab(self, tab, tab_name):
        canvas = Canvas(
            tab,
            bg="#FFFFFF",
            height=150,  # Reduced height to accommodate other widgets
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill="both", expand=False)
        canvas.create_rectangle(
            0.0,
            0.0,
            1024.0,
            150.0,
            fill="#006DFF",
            outline=""
        )
        
        canvas.create_text(
            20.0,
            670.0,
            anchor="nw",
            text="SGD",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )
        
        self.image_voltar = PhotoImage(
            file=self.relative_to_assets("voltar.png"))
        voltar = Button(
            image=self.image_voltar,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_principal,
            relief="flat"
        )
        voltar.place(
            x=417.0,
            y=668.0,
            width=189.0,
            height=50.0
        )
        # Adiciona a imagem na aba
        #self.add_image_toy_tab(canvas)
        #self.add_image_rec_tab(canvas)
        #self.add_entry_in_tab(tab, tab_name)
    def load_image(self):
        # Carrega a imagem apenas uma vez
        image_toy2 = self.relative_to_assets("toy2.png")
        self.image_toy2 = PhotoImage(file=image_toy2)
        image_rectangle5 = self.relative_to_assets("rectangle5.png")
        self.image_rectangle5 = PhotoImage(file=image_rectangle5)
    def add_image_toy_tab(self, canvas):
        canvas.create_image(
            920.0,
            650.0,
            image=self.image_toy2)
    def add_image_rec_tab(self, canvas):
        canvas.create_image(
        100.0,
        100.0,
        image=self.image_rectangle5
        )
    def add_entry_in_tab(self, tab, tab_name):
        # Cria uma caixa de entrada (entry) na mesma posição onde a imagem foi desenhada
        entry = Mascara(tab, formato='nome', x=100, y=100, texto=tab_name)
        return entry