from tkinter import Entry

def on_entry_click(event, entry, texto):
    if entry.get() == texto:
        entry.delete(0, "end") # Remove o texto padrão
        entry.insert(0, '') # Insere um texto vazio
        entry.config(fg='black') # Muda a cor do texto para preto

def on_focusout(event, entry, texto, senha=False):
    if entry.get() == '':
        entry.insert(0, texto)
        entry.config(fg='grey') # Muda a cor do texto para cinza
        if senha:
            entry.config(show='')  # Remove a configuração para mostrar asteriscos se o campo de senha estiver vazio

def criar_campo_de_entrada(root, x, y, texto, obrigatorio=False, senha=False, width=200, height=20):
    entry = Entry(root, fg='grey', show='' if senha else None)
    
    # Adiciona um asterisco se o campo for obrigatório
    if obrigatorio:
        texto = texto + " *"
    
    entry.insert(0, texto)
    entry.bind('<FocusIn>', lambda event: on_entry_click(event, entry, texto))
    entry.bind('<FocusOut>', lambda event: on_focusout(event, entry, texto, senha))
    if senha:
        entry.bind('<Key>', lambda event: entry.config(show='*'))    
    entry.place(x=x, y=y, width=width, height=height)
    return entry