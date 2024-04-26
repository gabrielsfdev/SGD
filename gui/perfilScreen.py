from tkinter import Button, PhotoImage, messagebox
import tkinter as tk
from photo import Photo
import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from app.services import Sessao, Mascara, AtualizaCadastro
from app.utils.cep_utilities import busca_cep, verifica_cep
from app.utils.cpf_utilities import valida_cpf
import json


class Perfil(Photo):
    def __init__(self, controller):
        super().__init__(controller)
        self.recupera_usuario()
        self.create_canvas()
        self.draw_rectangle()
        self.criar_imagem()
        self.criar_texto()
        self.create_entries()
        self.create_buttons()

    def draw_rectangle(self):
        self.canvas.create_rectangle(0, 0, 1024.0, 768.0, fill="#006DFF", outline="")

    def criar_imagem(self):
        self.image_photo2 = PhotoImage(
            file=self.relative_to_assets("photo2.png"))
        self.photo2 = self.canvas.create_image(
            512.0,
            124.0,
            image=self.image_photo2
        )

        self.image_rectangle2 = PhotoImage(
            file=self.relative_to_assets("rectangle2.png"))
        self.rectangle2 = self.canvas.create_image(
            345.0,
            282.0,
            image=self.image_rectangle2
        )

        self.image_rectangle3 = PhotoImage(
            file=self.relative_to_assets("rectangle3.png"))
        self.rectangle3 = self.canvas.create_image(
            783.0,
            282.0,
            image=self.image_rectangle3
        )

        self.image_rectangle4 = PhotoImage(
            file=self.relative_to_assets("rectangle4.png"))
        self.rectangle4 = self.canvas.create_image(
            216.0,
            362.0,
            image=self.image_rectangle4
        )

        self.rectangle4 = self.canvas.create_image(
            500.0,
            362.0,
            image=self.image_rectangle4
        )

        self.rectangle4 = self.canvas.create_image(
            784.0,
            362.0,
            image=self.image_rectangle4
        )

        self.image_rectangle5 = PhotoImage(
            file=self.relative_to_assets("rectangle5.png"))
        self.rectangle5 = self.canvas.create_image(
            292.0,
            462.0,
            image=self.image_rectangle5
        )

        self.image_rectangle6 = PhotoImage(
            file=self.relative_to_assets("rectangle6.png"))
        self.rectangle6 = self.canvas.create_image(
            587.0,
            462.0,
            image=self.image_rectangle6
        )

        self.rectangle4 = self.canvas.create_image(
            806.0,
            462.0,
            image=self.image_rectangle4
        )

        self.rectangle3 = self.canvas.create_image(
            240.0,
            542.0,
            image=self.image_rectangle3
        )

        self.image_rectangle7 = PhotoImage(
            file=self.relative_to_assets("rectangle7.png"))
        self.rectangle7 = self.canvas.create_image(
            606.0,
            542.0,
            image=self.image_rectangle7
        )

        self.image_rectangle8 = PhotoImage(
            file=self.relative_to_assets("rectangle8.png"))
        self.rectangle8 = self.canvas.create_image(
            858.0,
            542.0,
            image=self.image_rectangle8
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
    
    def create_buttons(self):
        self.adicionar_foto = self.canvas.create_text(
            473.0,
            189.0,
            anchor="nw",
            text="Adicionar Foto",
            fill="#FFFFFF",
            font=("Abel Regular", 14 * -1)
        )
        self.bind_text_events_perfil(self.adicionar_foto)


        self.image_voltar = PhotoImage(
            file=self.relative_to_assets("voltar.png"))
        self.voltar = Button(
            image=self.image_voltar,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_principal,
            relief="flat"
        )
        self.voltar.place(
            x=556.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

        self.image_salvar = PhotoImage(
            file=self.relative_to_assets("salvar.png"))
        self.salvar = Button(
            image=self.image_salvar,
            borderwidth=0,
            highlightthickness=0,
            command=self.salvar_multiple_commands,
            relief="flat"
        )
        self.salvar.place(
            x=765.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

    def create_entries(self):        
        self.entryName = Mascara(self, formato='nome', x=100, y=268.0, texto=self.dados_usuario.nome_usuario)
        self.entryBirthdate = Mascara(self, formato="date", tamanho_max=8, x=642, y=268.0, texto=self.dados_usuario.datanascimento.strftime('%d/%m/%Y'))
        self.entryCPF = Mascara(self, formato="cpf", tamanho_max=11, x=100, y=348.0, texto=self.dados_usuario.cpf_usuario, obrigatorio=True)
        self.entryPhonenumber = Mascara(self, formato="telefone", tamanho_max=11, x=384, y=348.0, texto=self.dados_usuario.numero_telefone)
        self.entryCEP = Mascara(self, formato="cep", tamanho_max=8, x=668, y=348, texto=self.dados_usuario.cep, obrigatorio=True)
        self.entryCEP.entrada.bind("<FocusOut>", self.preenche_endereco)
        self.entryStreet = Mascara(self, formato='nome', x=100.0, y=448.0, texto=self.dados_usuario.logradouro)
        self.entryNumber = Mascara(self, formato='nome', x=536.0, y=448.0, texto=self.dados_usuario.numero, width=80)
        self.entryStreet2 = Mascara(self, formato='nome', x=690.0, y=448.0, texto=self.dados_usuario.complemento)
        self.entryNeighborhood = Mascara(self, formato='nome', x=100.0, y=528.0, texto=self.dados_usuario.bairro)
        self.entryCity = Mascara(self, formato='nome', x=433.0, y=528.0, texto=self.dados_usuario.nome_cidade)
        self.entryUF = Mascara(self, formato='nome', x=831.0, y=528.0, texto=self.dados_usuario.uf, width=50)

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        open = PagPrincipal(self)
        open.run()

    def open_adicionar_foto(self):
        self.upload_image()

    def recupera_usuario(self):
        usuario = Sessao()
        try:
            dados_usuario = usuario.recupera_dados()
            self.dados_usuario = dados_usuario['usuario']
        except:
            messagebox.showerror("Falha", dados_usuario)
            self.open_principal
            
    def salvar_multiple_commands(self):
        if self.valida_cpf():
            if self.verifica_cep():
                self.atualizar_usuario()

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
    
    def atualizar_usuario(self):
        novos_dados = {
        'nome_usuario': self.entryName.get(self.dados_usuario.nome_usuario),
        'datanascimento': self.entryBirthdate.get(self.dados_usuario.datanascimento.strftime('%d/%m/%Y')),
        'cpf_usuario': self.entryCPF.get(self.dados_usuario.cpf_usuario),
        'numero_telefone': self.entryPhonenumber.get(self.dados_usuario.numero_telefone),
        'cep': self.entryCEP.get(self.dados_usuario.cep),
        'logradouro': self.entryStreet.get(self.dados_usuario.logradouro),
        'numero': self.entryNumber.get(self.dados_usuario.numero),
        'complemento': self.entryStreet2.get(self.dados_usuario.complemento),
        'bairro': self.entryNeighborhood.get(self.dados_usuario.bairro),
        'nome_cidade': self.entryCity.get(self.dados_usuario.nome_cidade),
        'uf': self.entryUF.get(self.dados_usuario.uf)
        }
        atualiza = AtualizaCadastro()
        try:
            update = atualiza.atualiza_cadastro(self.dados_usuario, novos_dados)
            messagebox.showinfo(update)
        except:
            messagebox.showerror("Falha", update)

    def run(self):
        self.mainloop()

controller = True
app = Perfil(controller)
app.mainloop()