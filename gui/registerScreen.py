from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage
import inputField


class Register(tk.Tk):
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
        self.canvas.create_image(512.0, 384.0, image=self.image_blue_screen2)

        self.image_rectangle2 = PhotoImage(
            file=self.relative_to_assets("rectangle2.png"))
        self.rectangle2 = self.canvas.create_image(
            512.0,
            101.0,
            image=self.image_rectangle2
        )

        self.image_rectangle3 = PhotoImage(
            file=self.relative_to_assets("rectangle3.png"))
        self.rectangle3 = self.canvas.create_image(
            241.0,
            181.0,
            image=self.image_rectangle3
        )

        self.image_rectangle4 = PhotoImage(
            file=self.relative_to_assets("rectangle4.png"))
        self.rectangle4 = self.canvas.create_image(
            626.0,
            181.0,
            image=self.image_rectangle4
        )

        self.rectangle4 = self.canvas.create_image(
            292.0,
            281.0,
            image=self.image_rectangle4
        )

        self.image_rectangle5 = PhotoImage(
            file=self.relative_to_assets("rectangle5.png"))
        self.rectangle5 = self.canvas.create_image(
            589.0,
            281.0,
            image=self.image_rectangle5
        )

        self.image_rectangle6 = PhotoImage(
            file=self.relative_to_assets("rectangle6.png"))
        self.rectangle6 = self.canvas.create_image(
            808.0,
            281.0,
            image=self.image_rectangle6
        )

        self.image_rectangle7 = PhotoImage(
            file=self.relative_to_assets("rectangle7.png"))
        self.rectangle7 = self.canvas.create_image(
            251.0,
            361.0,
            image=self.image_rectangle7
        )

        self.image_rectangle8 = PhotoImage(
            file=self.relative_to_assets("rectangle8.png"))
        self.rectangle8 = self.canvas.create_image(
            626.0,
            361.0,
            image=self.image_rectangle8
        )

        self.image_rectangle9 = PhotoImage(
            file=self.relative_to_assets("rectangle9.png"))
        self.rectangle9 = self.canvas.create_image(
            877.0,
            361.0,
            image=self.image_rectangle9
        )

        self.rectangle3 = self.canvas.create_image(
            241.0,
            461.0,
            image=self.image_rectangle3
        )

        self.image_rectangle10 = PhotoImage(
            file=self.relative_to_assets("rectangle10.png"))
        self.rectangle10 = self.canvas.create_image(
            678.0,
            461.0,
            image=self.image_rectangle10
        )

        self.rectangle3 = self.canvas.create_image(
            241.0,
            541.0,
            image=self.image_rectangle3
        )

        self.rectangle3 = self.canvas.create_image(
            574.0,
            541.0,
            image=self.image_rectangle3
        )

    def create_entries(self):
        self.entryName = inputField.criar_campo_de_entrada(self, 101.0, 87.0, 'Nome Completo')
        self.entryBirthdate = inputField.criar_campo_de_entrada(self, 101.0, 167.0, 'Data de Nascimento')
        self.entryCPF = inputField.criar_campo_de_entrada(self, 435.0, 167.0, 'CPF')
        self.entryStreet = inputField.criar_campo_de_entrada(self, 101.0, 267.0, 'Logradouro')
        self.entryNumber = inputField.criar_campo_de_entrada(self, 536.0, 267.0, 'Número', False, 80)
        self.entryStreet2 = inputField.criar_campo_de_entrada(self, 692.0, 267.0, 'Complemento')
        self.entryNeighborhood = inputField.criar_campo_de_entrada(self, 101.0, 347.0, 'Bairro')
        self.entryCity = inputField.criar_campo_de_entrada(self, 456.0, 347.0, 'Cidade')
        self.entryUF = inputField.criar_campo_de_entrada(self, 849.0, 347.0, 'UF', False, 50)
        self.entryPhonenumber = inputField.criar_campo_de_entrada(self, 101.0, 447.0, 'Telefone')
        self.entryEmail = inputField.criar_campo_de_entrada(self, 433.0, 447.0, 'E-mail')
        self.entryPassword = inputField.criar_campo_de_entrada(self, 101.0, 527.0, 'Senha', True)
        self.entryPasswordagain = inputField.criar_campo_de_entrada(self, 432.0, 527.0, 'Repetir Senha', True)

    def create_buttons(self):
        self.voltar_image = PhotoImage(
            file=self.relative_to_assets("voltar.png"))
        voltar = Button(
            image=self.voltar_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_login,
            relief="flat"
        )
        voltar.place(
            x=522.0,
            y=642.0,
            width=189.0,
            height=50.0
        )

        self.cadastrar_image = PhotoImage(
            file=self.relative_to_assets("cadastrar.png"))
        cadastrar = Button(
            image=self.cadastrar_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("cadastrar clicked"),
            relief="flat"
        )
        cadastrar.place(
            x=731.0,
            y=642.0,
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
