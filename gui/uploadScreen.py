from tkinter import Button, PhotoImage
from baseApp import BaseApp


class Upload(BaseApp):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.draw_rectangle()
        #self.create_entries()
        self.create_buttons()
        #self.criar_imagem()
        #self.criar_texto()
    
    def draw_rectangle(self):
        self.canvas.create_rectangle(0, 0, 1024.0, 768.0, fill="#006DFF", outline="")
    
    def create_buttons(self):
        self.image_escolha_um_arquivo = PhotoImage(
            file=self.relative_to_assets("escolha_um_arquivo.png"))
        self.escolha_um_arquivo = Button(
            image=self.image_escolha_um_arquivo,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("escolha_um_arquivo clicked"),
            relief="flat"
        )
        self.escolha_um_arquivo.place(
            x=209.0,
            y=358.0,
            width=606.0,
            height=79.0
        )

        self.image_fazer_upload = PhotoImage(
            file=self.relative_to_assets("fazer_upload.png"))
        self.fazer_upload = Button(
            image=self.image_fazer_upload,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("fazer_upload clicked"),
            relief="flat"
        )
        self.fazer_upload.place(
            x=313.0,
            y=487.0,
            width=398.0,
            height=79.0
        )

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
            x=765.0,
            y=668.0,
            width=189.0,
            height=50.0
        )

        self.canvas.create_text(
            382.0,
            87.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 128 * -1)
        )

        self.canvas.create_text(
            45.0,
            686.0,
            anchor="nw",
            text="SGD",
            fill="#FFFFFF",
            font=("AbhayaLibre Regular", 40 * -1)
        )

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        open = PagPrincipal(self)
        open.run()

    def run(self):
        self.mainloop()