from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, Label, Checkbutton, IntVar, messagebox
import inputField


class Login(tk.Tk):
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

        self.image_blue_screen1 = PhotoImage(
            file=self.relative_to_assets("blue_screen1.png"))
        self.blue_screen1 = self.canvas.create_image(
            251.0,
            384.0,
            image=self.image_blue_screen1
        )

        self.image_folders = PhotoImage(
            file=self.relative_to_assets("folders.png"))
        self.folders = self.canvas.create_image(
            251.0,
            235.0,
            image=self.image_folders
        )

        self.image_rectangle1 = PhotoImage(
            file=self.relative_to_assets("rectangle1.png"))

        self.rectangle1 = self.canvas.create_image(
            762.0,
            362.0,
            image=self.image_rectangle1
        )

        self.rectangle1 = self.canvas.create_image(
            762.0,
            442.0,
            image=self.image_rectangle1
        )

        # Texto "Lembrar minha senha"
        lembrar_minha_senha_text = "Lembrar minha senha"
        lembrar_minha_senha = Label(
            self,
            text=lembrar_minha_senha_text,
            bg="#FFFFFF",
            fg="#000000",  # Cor do texto
            font=("Arial", 12),  # Fonte e tamanho do texto
        )
        # Posição do texto
        lembrar_minha_senha.place(
            x=682.0,
            y=577.0,
            width=162.0,
            height=25.0
        )
    
    def create_entries(self):
         self.entryEmail = inputField.criar_campo_de_entrada(self, 633.0, 349.0, 'E-mail')
         self.entryPassword = inputField.criar_campo_de_entrada(self, 633.0, 429.0, 'Senha', True)

    def create_buttons(self):
        self.image_cadastre = PhotoImage(
        file=self.relative_to_assets("cadastre.png"))
        cadastre = Button(
        image=self.image_cadastre,
        borderwidth=0,
        highlightthickness=0,
        command=self.open_cadastre,
        relief="flat"
        )
        cadastre.place(
        x=822.0,
        y=30.0,
        width=149.0,
        height=41.0
        )
        cadastre.config(cursor='hand2')  # Define o cursor para uma mãozinha quando passar sobre o botão

        self.conectar_image = PhotoImage(
        file=self.relative_to_assets("conectar.png"))
        conectar = Button(
        image=self.conectar_image,
        borderwidth=0,
        highlightthickness=0,
        command=self.login,
        relief="flat"
        )
        conectar.place(
        x=622.0,
        y=497.0,
        width=280.0,
        height=50.0
        )

        # Variável para controlar o estado do Checkbutton
        check_var = IntVar()
        # Checkbutton "Lembrar minha senha"
        check_button = Checkbutton(
            self,
            variable=check_var,
            bg="#FFFFFF",
        )
        # Posição do Checkbutton
        check_button.place(
            x=660.0,
            y=577.0,
            width=25.0,
            height=25.0
        )

        self.image_Esqueci_minha_senha = PhotoImage(
        file=self.relative_to_assets("Esqueci_minha_senha.png"))
        Esqueci_minha_senha = Button(
        image=self.image_Esqueci_minha_senha,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Esqueci_minha_senha clicked"),
        relief="flat"
        )
        Esqueci_minha_senha.place(
        x=682.0,
        y=632.0,
        width=161.0,
        height=25.0
        )
        Esqueci_minha_senha.config(cursor='hand2')  # Define o cursor para uma mãozinha quando passar sobre o botão

    def login(self):
        username = self.entryEmail.get()
        password = self.entryPassword.get()
        result = self.controller.authenticate(username, password)
        if result:
            messagebox.showinfo("Login feito", "Boas vindas, " + username)
        else:
            messagebox.showerror("Falha no Login", "Usuário ou senha inválida")

    def open_cadastre(self):
        self.destroy()
        from registerScreen import Register
        Register(self).run()
