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
        self.blue_screen2 = self.canvas.create_image(
            512.0,
            384.0,
            image=self.image_blue_screen2
        )

        self.image_rectangle2 = PhotoImage(
            file=self.relative_to_assets("rectangle2.png"))
        self.rectangle2 = self.canvas.create_image(
            345.0,
            114.0,
            image=self.image_rectangle2
        )

        self.image_rectangle3 = PhotoImage(
            file=self.relative_to_assets("rectangle3.png"))
        self.rectangle3 = self.canvas.create_image(
            783.0,
            114.0,
            image=self.image_rectangle3
        )

        self.image_rectangle4 = PhotoImage(
            file=self.relative_to_assets("rectangle4.png"))
        self.rectangle4 = self.canvas.create_image(
            216.0,
            194.0,
            image=self.image_rectangle4
        )

        self.rectangle4 = self.canvas.create_image(
            500.0,
            194.0,
            image=self.image_rectangle4
        )

        self.rectangle4 = self.canvas.create_image(
            784.0,
            194.0,
            image=self.image_rectangle4
        )

        self.image_rectangle5 = PhotoImage(
            file=self.relative_to_assets("rectangle5.png"))
        self.rectangle5 = self.canvas.create_image(
            292.0,
            294.0,
            image=self.image_rectangle5
        )

        self.image_rectangle6 = PhotoImage(
            file=self.relative_to_assets("rectangle6.png"))
        self.rectangle6 = self.canvas.create_image(
            587.0,
            294.0,
            image=self.image_rectangle6
        )

        self.rectangle4 = self.canvas.create_image(
            806.0,
            294.0,
            image=self.image_rectangle4
        )

        self.rectangle3 = self.canvas.create_image(
            240.0,
            374.0,
            image=self.image_rectangle3
        )

        self.image_rectangle7 = PhotoImage(
            file=self.relative_to_assets("rectangle7.png"))
        self.rectangle7 = self.canvas.create_image(
            606.0,
            374.0,
            image=self.image_rectangle7
        )

        self.image_rectangle8 = PhotoImage(
            file=self.relative_to_assets("rectangle8.png"))
        self.rectangle8 = self.canvas.create_image(
            858.0,
            374.0,
            image=self.image_rectangle8
        )

        self.rectangle3 = self.canvas.create_image(
            241.0,
            474.0,
            image=self.image_rectangle3
        )

        self.rectangle2 = self.canvas.create_image(
            679.0,
            474.0,
            image=self.image_rectangle2
        )

        self.rectangle3 = self.canvas.create_image(
            241.0,
            554.0,
            image=self.image_rectangle3
        )

        self.rectangle3 = self.canvas.create_image(
            575.0,
            554.0,
            image=self.image_rectangle3
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
        self.entryName = inputField.criar_campo_de_entrada(self, 100.0, 100.0, 'Nome Completo')
        self.entryBirthdate = inputField.criar_campo_de_entrada(self, 642.0, 100.0, 'Data de Nascimento')
        self.entryCPF = inputField.criar_campo_de_entrada(self, 100.0, 180.0, 'CPF')
        self.entryPhonenumber = inputField.criar_campo_de_entrada(self, 384.0, 180.0, 'Telefone')
        self.entryCEP = inputField.criar_campo_de_entrada(self, 668.0, 180.0, 'CEP')
        self.entryStreet = inputField.criar_campo_de_entrada(self, 100.0, 280.0, 'Logradouro')
        self.entryNumber = inputField.criar_campo_de_entrada(self, 536.0, 280.0, 'Número', False, 80)
        self.entryStreet2 = inputField.criar_campo_de_entrada(self, 690.0, 280.0, 'Complemento')
        self.entryNeighborhood = inputField.criar_campo_de_entrada(self, 100.0, 360.0, 'Bairro')
        self.entryCity = inputField.criar_campo_de_entrada(self, 433.0, 360.0, 'Cidade')
        self.entryUF = inputField.criar_campo_de_entrada(self, 831.0, 360.0, 'UF', False, 50)
        self.entryUsername = inputField.criar_campo_de_entrada(self, 100.0, 460.0, 'Nome de Usuário')
        self.entryEmail = inputField.criar_campo_de_entrada(self, 434.0, 460.0, 'E-mail')
        self.entryPassword = inputField.criar_campo_de_entrada(self, 100.0, 540.0, 'Senha', True)
        self.entryPasswordagain = inputField.criar_campo_de_entrada(self, 434.0, 540.0, 'Repetir Senha', True)

    def create_buttons(self):
        self.image_voltar = PhotoImage(
            file=self.relative_to_assets("voltar.png"))
        voltar = Button(
            image=self.image_voltar,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_login,
            relief="flat"
        )
        voltar.place(
            x=556.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

        self.image_cadastrar = PhotoImage(
            file=self.relative_to_assets("cadastrar.png"))
        cadastrar = Button(
            image=self.image_cadastrar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("cadastrar clicked"),
            relief="flat"
        )
        cadastrar.place(
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
        