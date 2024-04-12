from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import inputField

class RecuperarSenha(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.geometry("1024x768+200-50")
        self.configure(bg="#FFFFFF")
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / "assets" / "frame0"

        self.create_canvas()
        self.create_entries()
        self.create_buttons()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)
    
    def create_canvas(self):
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1024,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_blue_screen2 = PhotoImage(
            file=self.relative_to_assets("blue_screen2.png"))
        self.blue_screen2 = self.canvas.create_image(
            512.0,
            384.0,
            image=self.image_blue_screen2
        )

        self.image_rectangle2 = PhotoImage(
            file=self.relative_to_assets("rectangle2.png"))
        self.rectangle2 = self.canvas.create_image(
            511.0,
            273.0,
            image=self.image_rectangle2
        )

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