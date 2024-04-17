
# Verifica se o CPF é válido, de acordo com o cálculo dos dígitos
def valida_cpf(cpf):
    cpf = cpf.replace('.','').replace('-','')
    if not cpf or len(cpf) != 11 or not cpf.isdigit() or cpf == cpf[0] * 11:
        raise ValueError("O CPF informado está incorreto. Deve conter 11 dígitos numéricos e não ser sequencial.")

    def calcular_digito(digito):
        return sum(int(x) * y for x, y in zip(digito, range(len(digito)+1, 1, -1))) * 10 % 11 % 10

    d1 = calcular_digito(cpf[:9])
    d2 = calcular_digito(cpf[:10])

    if d1 != int(cpf[9]) or d2 != int(cpf[10]):
        raise ValueError("O CPF informado é inválido.")

    return formatar_cpf(cpf)


# Formata o CPF para o padrão XXX.XXX.XXX-XX
def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


