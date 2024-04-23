import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from tkinter import Button, PhotoImage, filedialog, messagebox
from baseApp import BaseApp
from app.services import Arquivo


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
            command=self.janela_selecao,
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
            command=self.upload,
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

    def janela_selecao(self):
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecionar Arquivo",
            filetypes=(
                        ('Todos os Arquivos', '*.*'),
                        ('Arquivos PDF', '*.pdf'),
                        ("Arquivos JPEG", "*.jpeg;*.jpg"),
                        ("Arquivos PNG", "*.png"))  # Tipos de arquivo
        )
        if caminho_arquivo:
            self.caminho_arquivo = caminho_arquivo
            print(f"Arquivo selecionado: {caminho_arquivo}")
        else:
            print("Nenhum arquivo foi selecionado.")
    
    def upload(self):
        salva_arquivo = Arquivo()
        try:
            result = salva_arquivo.upload_arquivo(self.caminho_arquivo)
            messagebox.showinfo('Sucesso', result['message'])
            self.destroy()
            open = Upload(self)
            open.run()
        except:
            messagebox.showerror("Falha no Upload", result)
            self.destroy()
            from loginScreen import Login
            open = Login(self)
            open.run()

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        open = PagPrincipal(self)
        open.run()

    def run(self):
        self.mainloop()