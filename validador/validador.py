import re
from datetime import date, timedelta



def validar_nome(nome):
    tamanho_nome = len(nome)
    if tamanho_nome <= 80:
        return nome
    else:
        print('nome invalido insira nome novamente!')

def validar_email(email):
    if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email):
        return email
    else:
        print("E-mail inválido")

def validar_cpf(cpf):

    if len(cpf) < 11:
        return False

    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False


    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    cpf = "{:0>11}".format(int(cpf))

    return re.sub("(\d{3})(\d{3})(\d{3})(\d{2})",
                  "\\1.\\2.\\3-\\4",
                  cpf)



def Valor_pagar(ValorAPegar, qtdparcelas):
    dia_simulacao = date.today()

    if qtdparcelas == 1:
        valorTotal = ValorAPegar
        jurosam = 0
        valorparcela = valorTotal
        calc_pagamento = dia_simulacao + timedelta(days=40)
        data_pagamento = calc_pagamento.strftime('%d/%m/%Y')

        return ValorAPegar, jurosam, valorparcela, valorTotal, data_pagamento

    else:
        jurosam = 1
        taxa = jurosam / 100
        valorTotal = ValorAPegar * pow((1 + taxa), qtdparcelas)
        juros = valorTotal - ValorAPegar
        valorparcela = valorTotal / qtdparcelas
        calc_pagamento = dia_simulacao + timedelta(days=45)
        data_pagamento = calc_pagamento.strftime('%d/%m/%Y')

        return valorTotal, juros, valorTotal, valorparcela, data_pagamento

def validar_telefone(telefone):
    tamanho_tel = len(telefone)

    if tamanho_tel == 11:
        telefone = "{:0>11}".format(int(telefone))
        return re.sub("(\d{2})(\d)(\d{4})(\d{4})",
                      "(\\1) \\2 \\3-\\4",
                      telefone)
    else:
        print('telefone invalido!')

