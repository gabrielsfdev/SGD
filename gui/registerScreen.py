import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
import tkinter as tk
from tkinter import Button, PhotoImage, messagebox
import inputField
from baseApp import BaseApp
import inputField
from app.services import Usuario
from app.services import Mascara
from app.utils.cep_utilities import busca_cep, verifica_cep
from app.utils.cpf_utilities import valida_cpf
import json


class Register(BaseApp):
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

    def criar_texto(self):
        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )


    def create_entries(self):
        self.entryName = Mascara(self, formato='nome', x=100, y=100, texto='Nome Completo')
        self.entryBirthdate = Mascara(self, formato="date", tamanho_max=8, x=642, y=100, texto='Data de Nascimento')
        self.entryCPF = Mascara(self, formato="cpf", tamanho_max=11, x=100, y=180, texto='CPF', obrigatorio=True)
        self.entryPhonenumber = Mascara(self, formato="telefone", tamanho_max=11, x=384, y=180, texto="Telefone")
        self.entryCEP = Mascara(self, formato="cep", tamanho_max=8, x=668, y=180, texto='CEP', obrigatorio=True)
        self.entryCEP.entrada.bind("<FocusOut>", self.preenche_endereco)
        self.entryStreet = Mascara(self, formato='nome', x=100.0, y=280.0, texto='Logradouro')
        self.entryNumber = Mascara(self, formato='nome', x=536.0, y=280.0, texto='Número', width=80)
        self.entryStreet2 = Mascara(self, formato='nome', x=690.0, y=280.0, texto='Complemento')
        self.entryNeighborhood = Mascara(self, formato='nome', x=100.0, y=360.0, texto='Bairro')
        self.entryCity = Mascara(self, formato='nome', x=433.0, y=360.0, texto='Cidade')
        self.entryUF = Mascara(self, formato='nome', x=831.0, y=360.0, texto='UF', width=50)
        self.entryUsername = Mascara(self, formato='nome', x=100.0, y=460.0, texto='Nome de Usuário', obrigatorio=True)
        self.entryEmail = Mascara(self, formato='nome', x=434.0, y=460.0, texto='E-mail', obrigatorio=True)
        self.entryPassword = Mascara(self, formato='nome', x=100.0, y=540.0, texto='Senha', obrigatorio=True, senha=True)
        self.entryPasswordagain = Mascara(self, formato='nome', x=434.0, y=540.0, texto='Repetir Senha', obrigatorio=True, senha=True)

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
            command=self.cadastrar_multiple_commands,
            relief="flat"
        )
        cadastrar.place(
            x=765.0,
            y=668.0,
            width=189.0,
            height=50.0
        )
    def cadastrar_multiple_commands(self):
        if self.valida_cpf():
            if self.verifica_cep():
                self.cadastrar_usuario()

    def verifica_cep(self, event=None):
        cep = self.entryCEP.get('CEP')
        try:
            verifica_cep(cep)
            return True
        except ValueError as e:
            messagebox.showerror('Erro de Verificação', e)
            self.entryCEP.delete(0, tk.END)
            self.entryCEP.focus_set()
        
    def valida_cpf(self, event=None):
        cpf = self.entryCPF.get('CPF')
        try:
            valida_cpf(cpf)
            return True
        except ValueError as e:
            messagebox.showerror('Erro Validação CPF', e)
            self.entryCPF.delete(0, tk.END)
            self.entryCPF.focus_set()

    def preenche_endereco(self, event=None):
        cep = self.entryCEP.get('CEP')
        try:
            dados_cep = busca_cep(cep)
            if dados_cep.status_code == 200:
                json_cep = json.loads(dados_cep.content.decode('utf-8'))
                
                if len(json_cep) == 1:
                    messagebox.showerror('CEP não localizado', 'CEP não localizado. Preencha o endereço manualmente')
                    cep = cep[:5] + '-' + cep[5:]
                    
                    self.entryCEP.delete(0, tk.END)
                    self.entryCEP.insert(0, cep)
                    self.entryStreet.delete(0, tk.END)
                    self.entryNeighborhood.delete(0, tk.END)
                    self.entryCity.delete(0, tk.END)
                    self.entryCity.delete(0, tk.END)
                    self.entryUF.delete(0, tk.END)
                    
                    self.entryStreet.focus_set()
                else:
                    self.entryCEP.delete(0, tk.END)
                    self.entryCEP.insert(0, json_cep['cep'])
                    
                    self.entryStreet.delete(0, tk.END)
                    self.entryStreet.insert(0, json_cep['logradouro'])
                    self.entryStreet.entrada.config(fg='black')
                    
                    self.entryNeighborhood.delete(0, tk.END)
                    self.entryNeighborhood.insert(0, json_cep['bairro'])
                    self.entryNeighborhood.entrada.config(fg='black')
                    
                    self.entryCity.delete(0, tk.END)
                    self.entryCity.insert(0, json_cep['localidade'])
                    self.entryCity.entrada.config(fg='black')
                    
                    self.entryUF.delete(0, tk.END)
                    self.entryUF.insert(0, json_cep['uf'])
                    self.entryUF.entrada.config(fg='black')
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
        login = self.entryUsername.get()
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