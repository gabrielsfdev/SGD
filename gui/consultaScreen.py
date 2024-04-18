from tkinter import ttk
from baseTab import BaseTab

class Consulta(BaseTab):
    def __init__(self, controller):
        super().__init__(controller)
        self.create_canvas()
        self.create_notebook()
        self.load_image()  # Carrega a imagem apenas uma vez
        self.create_tabs()

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

        self.notebook = ttk.Notebook(self.canvas)  # Adicionando o notebook como filho do canvas
        self.notebook.pack(expand=True, fill="both")

    def create_tabs(self):
        self.tab_names = ['Nome', 'CPF', 'Telefone', 'CEP', 'Endereço', 'Bairro',
                          'Cidade', 'Estado', 'Outros']

        tab1 = ttk.Frame(self.notebook)
        tab2 = ttk.Frame(self.notebook)
        tab3 = ttk.Frame(self.notebook)
        tab4 = ttk.Frame(self.notebook)
        tab5 = ttk.Frame(self.notebook)
        tab6 = ttk.Frame(self.notebook)
        tab7 = ttk.Frame(self.notebook)
        tab8 = ttk.Frame(self.notebook)
        tab9 = ttk.Frame(self.notebook)

        self.notebook.add(tab1, text=self.tab_names[0])
        self.notebook.add(tab2, text=self.tab_names[1])
        self.notebook.add(tab3, text=self.tab_names[2])
        self.notebook.add(tab4, text=self.tab_names[3])
        self.notebook.add(tab5, text=self.tab_names[4])
        self.notebook.add(tab6, text=self.tab_names[5])
        self.notebook.add(tab7, text=self.tab_names[6])
        self.notebook.add(tab8, text=self.tab_names[7])
        self.notebook.add(tab9, text=self.tab_names[8])

        self.create_canvas_in_tab(tab1, self.tab_names[0])
        self.create_canvas_in_tab(tab2, self.tab_names[1])
        self.create_canvas_in_tab(tab3, self.tab_names[2])
        self.create_canvas_in_tab(tab4, self.tab_names[3])
        self.create_canvas_in_tab(tab5, self.tab_names[4])
        self.create_canvas_in_tab(tab6, self.tab_names[5])
        self.create_canvas_in_tab(tab7, self.tab_names[6])
        self.create_canvas_in_tab(tab8, self.tab_names[7])
        self.create_canvas_in_tab(tab9, self.tab_names[8])

    def open_principal(self):
        self.destroy()
        from principalScreen import PagPrincipal
        open = PagPrincipal(self)
        open.run()

    def run(self):
        self.mainloop()

controller = True
app = Consulta(controller)
app.mainloop()