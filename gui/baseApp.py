from tkinter import Canvas, Tk
from pathlib import Path

class BaseApp(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.geometry("1024x768+200-50")
        self.configure(bg="#FFFFFF")
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / "assets" / "frame0"

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
    
    def bind_text_events_login(self, text_id):
        self.canvas.tag_bind(text_id, "<Button-1>", self.on_text_click_login)
        self.canvas.tag_bind(text_id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(text_id, "<Leave>", self.on_leave)

    def bind_text_events_principal(self, text_id):
        self.canvas.tag_bind(text_id, "<Button-1>", self.on_text_click_principal)
        self.canvas.tag_bind(text_id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(text_id, "<Leave>", self.on_leave)

    def on_text_click_login(self, event):
        text_id = self.canvas.find_closest(event.x, event.y)[0]
        if text_id == self.cadastre:
            self.open_cadastre()
        elif text_id == self.esqueci_minha_senha:
            self.open_esqueceu_sua_senha()

    def on_text_click_principal(self, event):
        text_id = self.canvas.find_closest(event.x, event.y)[0]
        if text_id == self.adicionar_foto:
            self.open_adicionar_foto()
        elif text_id == self.desconectar:
            self.open_login()                
        elif text_id == self.upload_documentos:
            self.open_upload_documentos()
        elif text_id == self.editar_perfil:
            self.open_perfil()
        elif text_id == self.consultar_documentos:
            self.open_consultar_documentos()        

    def on_enter(self, event):
        self.canvas.config(cursor="hand2")

    def on_leave(self, event):
        self.canvas.config(cursor="")

    def underline_text(self, text_id):
        x0, y0, x1, y1 = self.canvas.bbox(text_id)
        self.canvas.create_line(x0, y1-2 , x1, y1-2 , fill="#006DFF", width=2)