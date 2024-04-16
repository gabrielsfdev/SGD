from tkinter import Button, PhotoImage
import inputField
from baseApp import BaseApp

class RecuperarSenha(BaseApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.draw_rectangle()
        self.criar_imagem()
        self.criar_texto()
        self.create_entries()
        self.create_buttons()
    
    def draw_rectangle(self):
        self.canvas.create_rectangle(0, 0, 1024.0, 768.0, fill="#006DFF", outline="")
    
    def criar_imagem(self):
        self.image_rectangle2 = PhotoImage(
            file=self.relative_to_assets("rectangle2.png"))
        self.rectangle2 = self.canvas.create_image(
            511.0,
            273.0,
            image=self.image_rectangle2
        )
    def criar_texto(self):
        self.canvas.create_text(
            158.0,
            76.0,
            anchor="nw",
            text="Recuperar senha",
            fill="#FFFFFF",
            font=("Abel Regular", 96 * -1)
        )

        self.canvas.create_text(
            209.0,
            348.0,
            anchor="nw",
            text="Após digitar seu e-mail, clique no botão enviar. A sua\nsenha cadastrada será enviada para o seu e-mail\ndigitado.",
            fill="#FFFFFF",
            font=("ABeeZee Regular", 24 * -1)
        )

        self.canvas.create_text(
            210.0,
            452.0,
            anchor="nw",
            text="Após conferir seu e-mail ou caso ainda não possua uma\nconta, clique no botão voltar. Você será direcionado a\npágina inicial.",
            fill="#FFFFFF",
            font=("ABeeZee Regular", 24 * -1)
        )

        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )

    def create_entries(self):
        self.entryEmail = inputField.criar_campo_de_entrada(self, 267.0, 259.0, 'Digite seu E-mail')
    
    def create_buttons(self):
        self.image_voltar = PhotoImage(
            file=self.relative_to_assets("voltar.png"))
        self.voltar = Button(
            image=self.image_voltar,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_login,
            relief="flat"
        )
        self.voltar.place(
            x=557.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

        self.image_enviar = PhotoImage(
            file=self.relative_to_assets("enviar.png"))
        self.enviar = Button(
            image=self.image_enviar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("enviar clicked"),
            relief="flat"
        )
        self.enviar.place(
            x=765.0,
            y=668.0,
            width=189.0,
            height=50.0
        )
    
    def open_login(self):
        self.destroy()
        from loginController import LoginController
        open = LoginController()
        open.run()

    def run(self):
        self.mainloop()