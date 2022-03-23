from validador.validador import *


def valida_data(data):

    if not validar_nome(data['nome']):
        return False

    if not validar_email(data['email']):
        return False

    if not validar_cpf(data['cpf']):
        return False
    if not validar_telefone(data['telefone']):
        return False
    if not Valor_pagar(data['valor'], data['qtd_parcela']):
        return False

    return True
