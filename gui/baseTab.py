from tkinter import Canvas, PhotoImage, Button
import inputField
from baseApp import BaseApp

class BaseTab(BaseApp):
    def create_canvas_in_tab(self, tab, tab_name):
        canvas = Canvas(
            tab,
            bg="#FFFFFF",
            height=768,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill="both", expand=True)
        canvas.create_rectangle(
            0.0,
            90.0,
            1024.0,
            560.0,
            fill="#006DFF",
            outline="")
        
        canvas.create_text(
            20.0,
            670.0,
            anchor="nw",
            text="SGD",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )
        
        self.image_lupa = PhotoImage(
            file=self.relative_to_assets("lupa.png"))
        self.lupa = Button(
            image=self.image_lupa,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("lupa clicked"),
            relief="flat"
        )
        self.lupa.place(
            x=645.0,
            y=384.0,
            width=56.52173614501953,
            height=50.0
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
        self.add_image_toy_tab(canvas)
        self.add_image_rec_tab(canvas)
        self.add_entry_in_tab(tab, tab_name)
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
        493.0,
        368.0,
        image=self.image_rectangle5
        )
    def add_entry_in_tab(self, tab, tab_name):
        # Cria uma caixa de entrada (entry) na mesma posição onde a imagem foi desenhada
        entry = inputField.criar_campo_de_entrada(tab, 320, 355, tab_name)
        return entry