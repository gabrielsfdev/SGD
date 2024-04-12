from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time


class PagPrincipal(tk.Tk):
    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.geometry("1024x768+200-50")
        self.configure(bg="#FFFFFF")
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / "assets" / "frame0"

        self.create_canvas()
        self.bind_text_events([self.adicionar_foto, self.desconectar, self.editar_perfil,
                               self.painel_central, self.gestao_documentos, self.upload_documentos,
                               self.compartilhamentos, self.notificacoes, self.historico,
                               self.ajuda])  # Adiciona os textos aqui
    
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

        self.image_blue_screen3 = PhotoImage(
            file=self.relative_to_assets("blue_screen3.png"))
        self.blue_screen3 = self.canvas.create_image(
            169.0,
            384.0,
            image=self.image_blue_screen3
        )

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

        self.adicionar_foto = self.canvas.create_text(
            130.0,
            122.5,
            anchor="nw",
            text="Adicionar Foto",
            fill="#FFFFFF",
            font=("Abel Regular", 14 * -1)
        )

        self.desconectar = self.canvas.create_text(
            111.0,
            150.5,
            anchor="nw",
            text="Desconectar",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.canvas.create_rectangle(
            22.0,
            205.0,
            314.9978766441345,
            207.11449573002756,
            fill="#FFFFFF",
            outline="")

        self.editar_perfil = self.canvas.create_text(
            23.0,
            227.114501953125,
            anchor="nw",
            text="Editar Perfil",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.painel_central = self.canvas.create_text(
            23.0,
            278.114501953125,
            anchor="nw",
            text="Painel Central",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.gestao_documentos = self.canvas.create_text(
            21.0,
            329.114501953125,
            anchor="nw",
            text="Gestão de Documentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.upload_documentos = self.canvas.create_text(
            21.0,
            380.114501953125,
            anchor="nw",
            text="Upload de Documentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.compartilhamentos = self.canvas.create_text(
            23.0,
            431.114501953125,
            anchor="nw",
            text="Compartilhamentos",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.notificacoes = self.canvas.create_text(
            23.0,
            482.114501953125,
            anchor="nw",
            text="Notificações e Alertas",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.historico = self.canvas.create_text(
            23.0,
            533.0,
            anchor="nw",
            text="Histórico",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.ajuda = self.canvas.create_text(
            23.0,
            584.0,
            anchor="nw",
            text="Ajuda",
            fill="#FFFFFF",
            font=("Abel Regular", 24 * -1)
        )

        self.canvas.create_rectangle(
            22.0,
            634.0,
            314.9978766441345,
            636.1144957300276,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )

    def bind_text_events(self, text_ids):
        for text_id in text_ids:
            self.canvas.tag_bind(text_id, "<Button-1>", self.on_text_click)
            self.canvas.tag_bind(text_id, "<Enter>", self.on_enter)
            self.canvas.tag_bind(text_id, "<Leave>", self.on_leave)

    def on_enter(self, event):
        self.canvas.config(cursor="hand2")

    def on_leave(self, event):
        self.canvas.config(cursor="")

    def on_text_click(self, event):
        text_id = self.canvas.find_closest(event.x, event.y)[0]
        for _ in range(1):  # Altere o número de piscadas conforme necessário
            self.canvas.itemconfig(text_id, fill="#000000")  # Altera para preto
            if text_id is self.desconectar:
                self.destroy()
                from loginController import LoginController
                open = LoginController()
                open.run()
            elif text_id is self.upload_documentos:
                self.destroy()
                from uploadScreen import Upload
                open = Upload(self)
                open.run()
            self.update()  # Atualiza a janela
            time.sleep(0.1)  # Aguarda um curto período
            self.canvas.itemconfig(text_id, fill="#FFFFFF")  # Altera para branco
            self.update()  # Atualiza a janela
            time.sleep(0.1)  # Aguarda um curto período

    def run(self):
        self.mainloop()
