import sys
import os
sys.path.append(os.getenv('CAMINHO_RAIZ_PROJETO'))
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
import inputField
from app.services import Usuario
from app.utils import *
import json


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
            141.0,
            image=self.image_rectangle2
        )

        self.image_rectangle3 = PhotoImage(
            file=self.relative_to_assets("rectangle3.png"))
        self.rectangle3 = self.canvas.create_image(
            241.0,
            221.0,
            image=self.image_rectangle3
        )

        self.image_rectangle4 = PhotoImage(
            file=self.relative_to_assets("rectangle4.png"))
        self.rectangle4 = self.canvas.create_image(
            626.0,
            221.0,
            image=self.image_rectangle4
        )
        
        self.image_rectangle5 = PhotoImage(
            file=self.relative_to_assets("rectangle5.png"))
        self.rectangle5 = self.canvas.create_image(
            150.0,
            301.0,
            image=self.image_rectangle5
        )

        self.image_rectangle6 = PhotoImage(
            file=self.relative_to_assets("rectangle6.png"))
        self.rectangle6 = self.canvas.create_image(
            370.0,
            301.0,
            image=self.image_rectangle6
        )

        self.rectangle5 = self.canvas.create_image(
            590.0,
            301.0,
            image=self.image_rectangle5
        )
        
        self.rectangle6 = self.canvas.create_image(
            808.0,
            301.0,
            image=self.image_rectangle6
        )

        self.image_rectangle7 = PhotoImage(
            file=self.relative_to_assets("rectangle7.png"))
        self.rectangle7 = self.canvas.create_image(
            251.0,
            381.0,
            image=self.image_rectangle7
        )

        self.image_rectangle8 = PhotoImage(
            file=self.relative_to_assets("rectangle8.png"))
        self.rectangle8 = self.canvas.create_image(
            640.0,
            381.0,
            image=self.image_rectangle8
        )

        self.image_rectangle9 = PhotoImage(
            file=self.relative_to_assets("rectangle9.png"))
        self.rectangle9 = self.canvas.create_image(
            898.0,
            381.0,
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

        self.rectangle6 = self.canvas.create_image(
            213.0,
            541.0,
            image=self.image_rectangle6
        )

        self.rectangle6 = self.canvas.create_image(
            512.0,
            541.0,
            image=self.image_rectangle6
        )

        self.rectangle6 = self.canvas.create_image(
            812.0,
            541.0,
            image=self.image_rectangle6
        )

    def create_entries(self):
        self.entryName = inputField.criar_campo_de_entrada(self, 101.0, 130.0, 'Nome Completo')
        self.entryBirthdate = inputField.criar_campo_de_entrada(self, 101.0, 210.0, 'Data de Nascimento')
        self.entryCPF = inputField.criar_campo_de_entrada(self, 435.0, 210.0, 'CPF')
        self.entryCEP = inputField.criar_campo_de_entrada(self, 101.0, 290.0, 'CEP', False, 80)
        self.entryCEP.bind("<FocusOut>", self.preenche_endereco)
        self.entryStreet = inputField.criar_campo_de_entrada(self, 250.0, 290.0, 'Logradouro')
        self.entryNumber = inputField.criar_campo_de_entrada(self, 536.0, 290.0, 'Número', False, 80)
        self.entryStreet2 = inputField.criar_campo_de_entrada(self, 692.0, 290.0, 'Complemento')
        self.entryNeighborhood = inputField.criar_campo_de_entrada(self, 101.0, 370.0, 'Bairro')
        self.entryCity = inputField.criar_campo_de_entrada(self, 476.0, 370.0, 'Cidade')
        self.entryUF = inputField.criar_campo_de_entrada(self, 869.0, 370.0, 'UF', False, 50)
        self.entryPhonenumber = inputField.criar_campo_de_entrada(self, 101.0, 450.0, 'Telefone')
        self.entryEmail = inputField.criar_campo_de_entrada(self, 433.0, 450.0, 'E-mail')
        self.entryLogin = inputField.criar_campo_de_entrada(self, 101.0, 530.0, 'Login')
        self.entryPassword = inputField.criar_campo_de_entrada(self, 401.0, 530.0, 'Senha', True)
        self.entryPasswordagain = inputField.criar_campo_de_entrada(self, 701.0, 530.0, 'Repetir Senha', True)

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
            command=self.cadastrar_usuario,
            relief="flat"
        )
        cadastrar.place(
            x=731.0,
            y=642.0,
            width=189.0,
            height=50.0
        )
        
    def preenche_endereco(self, event=None):
        cep = self.entryCEP.get()
        try:
            dados_cep = busca_cep(cep)
            if dados_cep.status_code == 200:
                json_cep = json.loads(dados_cep.content.decode('utf-8'))
                
                self.entryCEP.delete(0, tk.END)
                self.entryCEP.insert(0, json_cep['cep'])
                
                self.entryStreet.delete(0, tk.END)
                self.entryStreet.insert(0, json_cep['logradouro'])
                
                self.entryNeighborhood.delete(0, tk.END)
                self.entryNeighborhood.insert(0, json_cep['bairro'])
                
                self.entryCity.delete(0, tk.END)
                self.entryCity.insert(0, json_cep['localidade'])
                
                self.entryUF.delete(0, tk.END)
                self.entryUF.insert(0, json_cep['uf'])
        except Exception as e:
            messagebox.showerror("Erro de Busca por CEP", str(e))
            self.entryCEP.focus_set()

    def cadastrar_usuario(self):
        name = self.entryName.get()
        birthdate = self.entryBirthdate.get()
        cpf = self.entryCPF.get()
        cep = self.entryCEP.get()
        street = self.entryStreet.get()
        number = self.entryNumber.get()
        street2 = self.entryStreet2.get()
        bairro = self.entryNeighborhood.get()
        city = self.entryCity.get()
        uf = self.entryUF.get()
        phone = self.entryPhonenumber.get()
        email = self.entryEmail.get()
        login = self.entryLogin.get()
        pwd = self.entryPassword.get()
        pwd2 = self.entryPassword.get()
        
        usuario = Usuario(
        nome = name,
        cpf = cpf,
        datanascimento = birthdate,
        login = login,
        senha = pwd
        )
        resultado = usuario.registrar_usuario(
            telefone = phone,
            email = email,
            cep = cep,
            logradouro = street,
            numero = number,
            complemento = street2,
            bairro = bairro,
            idcidade = 1
        )
        messagebox.showinfo("Sucesso", resultado) 
    
    def open_login(self):
        self.destroy()
        from loginController import LoginController
        open = LoginController()
        open.run()

    def run(self):
        self.mainloop()

controller = True
app = Register(controller)
app.mainloop()