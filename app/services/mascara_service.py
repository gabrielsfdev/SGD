import tkinter as tk

class Mascara:
    def __init__(self, master, formato, placeholder="", tamanho_max=None, **kwargs):
        self.entrada = tk.Entry(master, **kwargs)
        self.formato = formato
        self.placeholder = placeholder
        self.tamanho_max = tamanho_max
        self.entrada.bind("<KeyRelease>", self.evento)
        self.entrada.bind("<FocusIn>", self.on_focus_in)
        self.entrada.bind("<Enter>", self.on_focus_in)
        self.entrada.bind("<FocusOut>", self.on_focus_out)
        self.set_placeholder()
        if self.tamanho_max:
            vcmd = (master.register(self.on_validate), '%P')
            self.entrada.config(validate="key", validatecommand=vcmd)
            
    def on_validate(self, P):
        digits = ''.join(filter(str.isdigit, P))
        return len(digits) <= self.tamanho_max

    def on_focus_in(self, event=None):
        if self.entrada.get() == self.placeholder:
            self.entrada.delete(0, "end")
    
    def valida_tamanho(self, novo_texto):
        return len(novo_texto) <= self.tamanho_max

    def evento(self, event=None):
        texto_atual = ''.join(filter(str.isdigit, self.entrada.get()))
        if texto_atual == self.placeholder:
            self.entrada.delete(0, 'end')
        novo_texto = self.aplica_mascara(texto_atual)
        self.entrada.config(fg='black')
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, novo_texto)

    def aplica_mascara(self, texto):
        texto = ''.join(filter(str.isdigit, texto))
        if self.formato == "date":
            if len(texto) > 4:
                texto = texto[:2] + '/' + texto[2:4] + '/' + texto[4:]
            elif len(texto) > 2:
                texto = texto[:2] + '/' + texto[2:]
        elif self.formato == "cpf":
            if len(texto) > 9:
                texto = texto[:3] + '.' + texto[3:6] + '.' + texto[6:9] + '-' + texto[9:11]
            elif len(texto) > 6:
                texto = texto[:3] + '.' + texto[3:6] + '.' + texto[6:]
            elif len(texto) > 3:
                texto = texto[:3] + '.' + texto[3:]
        elif self.formato == "cep":
            if len(texto) > 5:
                texto = texto[:5] + '-' + texto[5:8]
        elif self.formato == "telefone":
            if len(texto) > 10:
                texto = '(' + texto[:2] + ')' + texto[2:7] + '-' + texto[7:]
            elif len(texto) > 9:
                texto = '(' + texto[:2] + ')' + texto[2:6] + '-' + texto[6:]
            elif len(texto) > 7:
                texto = '(' + texto[:2] + ')' + texto[2:6] + '-' + texto[6:]
            elif len(texto) > 2:
                texto = '(' + texto[:2] + ')' + texto[2:]
        return texto

    def on_focus_out(self, event=None):
        if not self.entrada.get():
            self.set_placeholder()

    def set_placeholder(self):
        self.entrada.insert(0, self.placeholder)
        self.entrada.config(fg='grey')

    def delete(self, first, last=None):
        self.entrada.delete(first, last)

    def insert(self, index, string):
        self.entrada.insert(index, string)
        
    def focus_set(self):
        self.entrada.focus_set()

    def grid(self, **kwargs):
        self.entrada.grid(**kwargs)

    def get(self):
        text = self.entrada.get()
        if text == self.placeholder or not text.strip():
            return ""
        return self.entrada.get().strip()