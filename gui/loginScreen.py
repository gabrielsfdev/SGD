from tkinter import Button, PhotoImage, Checkbutton, IntVar, messagebox
from baseApp import BaseApp
import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from app.services import Usuario, Sessao
from app.utils import *
from app.services import Mascara


class Login(BaseApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.draw_rectangle()
        self.create_entries()
        self.create_buttons()
        self.criar_imagem()
        self.criar_texto()
        self.main()
    
    def draw_rectangle(self):
        self.canvas.create_rectangle(0, 0, 502.0, 768.0, fill="#006DFF", outline="")

    def criar_imagem(self):
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
    
    def criar_texto(self):
        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )
        self.canvas.create_text(
            624.0,
            144.0,
            anchor="nw",
            text="SGD",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 128 * -1)
        )
        
        self.canvas.create_text(
            685.0,
            580.0,
            anchor="nw",
            text="Lembrar minha senha",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 15 * -1)
        )

        self.cadastre = self.canvas.create_text(
            822,  # Posição x
            30,  # Posição y
            anchor="nw",  # Âncora no canto superior esquerdo
            text="Cadastre-se",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 30 * -1),
        )
        
        self.underline_text(self.cadastre)
        self.bind_text_events_login(self.cadastre)
        

        self.esqueci_minha_senha = self.canvas.create_text(
            660.0,
            632.0,
            anchor="nw",
            text="Esqueci minha senha",
            fill="#006DFF",
            font=("AbhayaLibre Regular", 20 * -1)
        )
        self.underline_text(self.esqueci_minha_senha)
        self.bind_text_events_login(self.esqueci_minha_senha)

    def create_entries(self):
        self.entryUsername = Mascara(self, formato='nome', x=633.0, y=349.0, texto='Nome de Usuário')
        self.entryPassword = Mascara(self, formato='nome', x=633.0, y=429.0, texto='Senha', senha=True)

    def create_buttons(self):
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
    
    def login(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get()
        usuario = Usuario(username, password)
        realizar_login = usuario.login_usuario()
        
        if realizar_login['success']:
            messagebox.showinfo('Sucesso', f'{realizar_login['message']}\nBem vindo {realizar_login['usuario'].nome_usuario}')
            self.destroy()
            from principalScreen import PagPrincipal
            PagPrincipal(self).run()
        else:
            messagebox.showerror("Falha no Login", realizar_login['message'])

    def open_cadastre(self):
        self.destroy()
        from registerScreen import Register
        Register(self).run()

    def open_esqueceu_sua_senha(self):
        self.destroy()
        from recuperarSenhaScreen import RecuperarSenha
        RecuperarSenha(self).run()
    
    def main(self):
        sessao = Sessao()
        if sessao.usuario_logado():
            usuario = sessao.carrega_sessao()
            messagebox.showinfo("Sucesso", f"Bem-vindo {usuario['nome_usuario']}!")
            self.destroy()
            from principalScreen import PagPrincipal
            PagPrincipal(self).run()
