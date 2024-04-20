import tkinter as tk

class Mascara:
    def __init__(self, master, formato, tamanho_max=None, **kwargs):
        self.formato = formato
        self.tamanho_max = tamanho_max
        self.criar_entrada(master, **kwargs)
        if self.tamanho_max:
            vcmd = (master.register(self.on_validate), '%P')
            self.entrada.config(validate="key", validatecommand=vcmd)
            
    def on_validate(self, P):
        digits = ''.join(filter(str.isdigit, P))
        return len(digits) <= self.tamanho_max

    def on_focus_in(self, event, texto):
        if self.entrada.get() == texto:
            self.entrada.delete(0, "end")
            self.entrada.insert(0, '') 
            self.entrada.config(fg='black')
    
    def valida_tamanho(self, novo_texto):
        return len(novo_texto) <= self.tamanho_max

    def evento(self, event, formato, texto):
        if formato in ['date', 'cpf', 'cep', 'telefone']:
            texto_atual = ''.join(filter(str.isdigit, self.entrada.get()))
            if texto_atual == texto:
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

    def on_focus_out(self, event, texto, senha):
        if self.entrada.get() == '':
            self.entrada.insert(0, texto)
            self.entrada.config(fg='grey') # Muda a cor do texto para cinza
            if senha:
                self.entrada.config(show='')

    def delete(self, first, last=None):
        self.entrada.delete(first, last)

    def insert(self, index, string):
        self.entrada.insert(index, string)
        
    def focus_set(self):
        self.entrada.focus_set()

    def grid(self, **kwargs):
        self.entrada.grid(**kwargs)

    def get(self, texto):
        list_placeholder = [
            'Nome Completo','Data de Nascimento','CPF','CPF*',
            'Telefone','CEP','CEP*','Logradouro','Número','Complemento','Bairro',
            'Cidade','UF','Nome de Usuário','E-mail','Senha','Repetir Senha',
            'Nome do Documento', 'Data Criação Inicial', 'Data Criação Final',
            'Nome da Pessoa no Documento', 'CPF da Pessoa no Documento'
            ]
        text = self.entrada.get()
        if text == texto and text in list_placeholder:
            return ""
        return text.strip()
    
    def criar_entrada(self, master, x, y, texto, obrigatorio=False, senha=False, width=200, height=25):
        self.entrada = tk.Entry(master, fg='grey', show='' if senha else None)
        
        # Adiciona um asterisco se o campo for obrigatório
        if obrigatorio and texto in ['Data de Nascimento', 'CPF', 'CEP', 'Telefone']:
            texto = texto + "*"

        self.entrada.insert(0, texto)
        self.entrada.bind("<KeyRelease>", lambda event: self.evento(event, self.formato, texto))
        self.entrada.bind('<FocusIn>', lambda event: self.on_focus_in(event, texto))
        self.entrada.bind('<FocusOut>', lambda event: self.on_focus_out(event, texto, senha))
        if senha:
            self.entrada.bind('<Key>', lambda event: self.entrada.config(show='*'))    
        self.entrada.place(x=x, y=y, width=width, height=height)