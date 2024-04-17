from tkinter import PhotoImage
from baseApp import BaseApp

class PagPrincipal(BaseApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.draw_rectangle()
        self.criar_imagem()
        self.criar_texto()
        self.create_button()
    
    def draw_rectangle(self):
        self.canvas.create_rectangle(0, 0, 338.0, 768.0, fill="#006DFF", outline="")

        self.canvas.create_rectangle(
            22.0,
            634.0,
            314.9978766441345,
            636.1144957300276,
            fill="#FFFFFF",
            outline="")
        
        self.canvas.create_rectangle(
            22.0,
            205.0,
            314.9978766441345,
            207.11449573002756,
            fill="#FFFFFF",
            outline="")
    
    def criar_imagem(self):
        self.image_toy1 = PhotoImage(
            file=self.relative_to_assets("toy1.png"))
        self.toy1 = self.canvas.create_image(
            855.0,
            384.0,
            image=self.image_toy1
        )

        self.image_photo1 = PhotoImage(
            file=self.relative_to_assets("photo1.png"))
        self.photo1 = self.canvas.create_image(
            169.0,
            81.0,
            image=self.image_photo1
        )

    def create_button(self):
        self.adicionar_foto = self.canvas.create_text(
            130.0,
            122.5,
            anchor="nw",
            text="Adicionar Foto",
            fill="#FFFFFF",
            font=("Abel Regular", 14 * -1)
        )
        self.bind_text_events_principal(self.adicionar_foto)

        self.desconectar = self.canvas.create_text(
            111.0,
            150.5,
            anchor="nw",
            text="Desconectar",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.desconectar)

        self.editar_perfil = self.canvas.create_text(
            23.0,
            227.114501953125,
            anchor="nw",
            text="Editar Perfil",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.editar_perfil)

        self.painel_central = self.canvas.create_text(
            23.0,
            278.114501953125,
            anchor="nw",
            text="Painel Central",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.painel_central)

        self.consultar_documentos = self.canvas.create_text(
            21.0,
            329.114501953125,
            anchor="nw",
            text="Consultar Documentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.consultar_documentos)

        self.upload_documentos = self.canvas.create_text(
            21.0,
            380.114501953125,
            anchor="nw",
            text="Upload de Documentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.upload_documentos)

        self.compartilhamentos = self.canvas.create_text(
            23.0,
            431.114501953125,
            anchor="nw",
            text="Compartilhamentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.compartilhamentos)

        self.notificacoes = self.canvas.create_text(
            23.0,
            482.114501953125,
            anchor="nw",
            text="Notificações e Alertas",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.notificacoes)

        self.historico = self.canvas.create_text(
            23.0,
            533.0,
            anchor="nw",
            text="Histórico",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.historico)

        self.ajuda = self.canvas.create_text(
            23.0,
            584.0,
            anchor="nw",
            text="Ajuda",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )
        self.bind_text_events_principal(self.ajuda)
    
    def criar_texto(self):
        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )
    
    def open_login(self):
        self.destroy()
        from loginController import LoginController
        open = LoginController()
        open.run()
    
    def open_upload_documentos(self):
        self.destroy()
        from uploadScreen import Upload
        open = Upload(self)
        open.run()

    def open_perfil(self):
        self.destroy()
        from perfilScreen import Perfil
        open = Perfil(self)
        open.run()

    def open_consultar_documentos(self):
        self.destroy()
        from consultaScreen import Consulta
        open = Consulta(self)
        open.run()

    def run(self):
        self.mainloop()