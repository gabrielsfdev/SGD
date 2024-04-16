from tkinter import Button, PhotoImage
import inputField
from baseApp import BaseApp


class Perfil(BaseApp):
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
        self.bind_text_events(self.adicionar_foto)


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
            command=lambda: print("salvar clicked"),
            relief="flat"
        )
        self.salvar.place(
            x=765.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

    def create_entries(self):
        self.entryName = inputField.criar_campo_de_entrada(self, 100.0, 268.0, 'Nome Completo')
        self.entryBirthdate = inputField.criar_campo_de_entrada(self, 642.0, 268.0, 'Data de Nascimento')
        self.entryCPF = inputField.criar_campo_de_entrada(self, 100.0, 348.0, 'CPF')
        self.entryPhonenumber = inputField.criar_campo_de_entrada(self, 384.0, 348.0, 'Telefone')
        self.entryCEP = inputField.criar_campo_de_entrada(self, 668.0, 348.0, 'CEP')
        self.entryStreet = inputField.criar_campo_de_entrada(self, 100.0, 448.0, 'Logradouro')
        self.entryNumber = inputField.criar_campo_de_entrada(self, 536.0, 448.0, 'Número', width=80)
        self.entryStreet2 = inputField.criar_campo_de_entrada(self, 690.0, 448.0, 'Complemento')
        self.entryNeighborhood = inputField.criar_campo_de_entrada(self, 100.0, 528.0, 'Bairro')
        self.entryCity = inputField.criar_campo_de_entrada(self, 433.0, 528.0, 'Cidade')
        self.entryUF = inputField.criar_campo_de_entrada(self, 831.0, 528.0, 'UF', width=50)

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        open = PagPrincipal(self)
        open.run()

    def run(self):
        self.mainloop()