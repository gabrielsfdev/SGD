from tkinter import ttk, PhotoImage, Button, messagebox
from baseTab import BaseTab
import tkinter as tk
import sys
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from app.services import Mascara, Arquivo

class Consulta(BaseTab):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.create_notebook()
        self.load_image()

    def create_notebook(self):
        self.notebook_style = ttk.Style()
        self.notebook_style.theme_create("CustomStyle", parent="alt", settings={
            "TNotebook.Tab": {
                "configure": {
                    "padding": [20, 5],
                    "font": ('Abel Regular', 18),
                    "foreground": "#006DFF",
                    "background": "#FFFFFF"
                },
                "map": {
                    "background": [("selected", "#006DFF")],
                    "foreground": [("selected", "#FFFFFF")]
                }
            }
        })
        self.notebook_style.theme_use("CustomStyle")
        self.notebook = ttk.Notebook(self.canvas)
        self.notebook.pack(expand=True, fill="both")
        self.create_tabs()

    def create_tabs(self):
        self.tab_names = ['Documento', 'Contrato']
        self.tabs = [ttk.Frame(self.notebook) for _ in self.tab_names]
        for tab, name in zip(self.tabs, self.tab_names):
            self.notebook.add(tab, text=name)
            self.create_canvas_in_tab(tab, name)
            self.create_search_and_treeview(tab)

    def create_search_and_treeview(self, tab):        
        self.nome_arquivo = Mascara(self, formato='nome', x=100, y=80.0, texto='Nome do Documento')
        self.data_inicial = Mascara(self, formato="date", tamanho_max=8, x=400, y=80.0, texto='Data Criação Inicial')
        self.data_final = Mascara(self, formato="date", tamanho_max=8, x=700, y=80.0, texto='Data Criação Final')
        self.nome_documento = Mascara(self, formato='nome', x=100.0, y=130.0, texto='Nome da Pessoa no Documento')
        self.cpf_documento = Mascara(self, formato="cpf", tamanho_max=11, x=400, y=130.0, texto='CPF da Pessoa no Documento')

        y_offset = 100

        image_lupa = PhotoImage(file=self.relative_to_assets("lupa.png"))
        lupa_button = Button(tab, image=image_lupa, borderwidth=0, highlightthickness=0, command=lambda: self.populate_treeview(tab), relief="flat")
        lupa_button.image = image_lupa
        lupa_button.place(x=750, y=y_offset, width=46, height=40)

        y_offset = 0

    def populate_treeview(self, tab, y_offset=0):
        if hasattr(self, 'tree'):
            self.tree.destroy()

        tree_style = ttk.Style()
        tree_style.configure("Treeview.Heading", background="#0078D7", foreground="white", font=('Abel Regular', 12))
        tree_style.map("Treeview.Heading", background=[('active', '#0066CC')])
        tree_style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        tree_style.map("Treeview", background=[('selected', '#0078D7')])

        tree = ttk.Treeview(tab, columns=('ID', 'Nome', 'Data Criação', 'Download'), show='headings')
        for col in ('ID', 'Nome', 'Data Criação'):
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor=tk.CENTER)

        tree.heading('Download', text='Download')
        tree.column('Download', width=100, anchor='center')

        data = self.campos_preenchidos()
        for item in data:
            iid = tree.insert('', 'end', values=(item.id, item.nome_arquivo, item.datacriacao, 'Baixar Arquivo ▼'))

        tree.pack(expand=True, fill='both', pady=(y_offset, 0))

        def on_download_click(event):
            try:
                region = self.tree.identify_region(event.x, event.y)
                column = self.tree.identify_column(event.x)
                if region == "cell" and column == "#4":
                    iid = self.tree.identify_row(event.y)
                    item = self.tree.item(iid)
                    item_id = item['values'][0]
                    item_nome = item['values'][1]
                    
                    arquivo = Arquivo()
                    download = arquivo.download_arquivo(item_id, item_nome)
                    
                    if download['success']:
                        messagebox.showinfo("Download Concluído", download['message'])
                    else:
                        messagebox.showerror("Erro no Download", download['message'])
            except Exception as e:
                messagebox.showerror("Erro no Download", f"Ocorreu um erro durante o download: {e}")

        tree.bind('<Button-1>', on_download_click)
        self.tree = tree
        
    def campos_preenchidos(self):
        valores_preenchidos = {
            'nome_arquivo': self.nome_arquivo.get('Nome do Documento'),
            'data_inicial': self.data_inicial.get('Data Criação Inicial'),
            'data_final': self.data_final.get('Data Criação Final'),
            'nome_documento': self.nome_documento.get('Nome da Pessoa no Documento'),
            'cpf_documento': self.cpf_documento.get('CPF da Pessoa no Documento')
        }
    
        dados_filtrados = {chave: valor for chave, valor in valores_preenchidos.items() if valor.strip()}
        if len(dados_filtrados) > 0:
            arquivo = Arquivo()
            try:
                busca = arquivo.busca_arquivo(**dados_filtrados)
                if busca['success']:
                    return busca['arquivos']
                else:
                    messagebox.showerror('Erro na Busca', busca['message'])
            except:
                messagebox.showerror('Erro na Busca', 'Você precisa preencher ao menos um campo.')

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        PagPrincipal(self).run()

    def run(self):
        self.mainloop()

controller = True
app = Consulta(controller)
app.mainloop()
