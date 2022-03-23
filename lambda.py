import logging
import base64
from pdf.gerarpdf import gera_pdf
from validadata.validadata import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    data = event.get("body")
    try:
        if valida_data(data):
            data["valor_total"], data["juros"], data["valorTotal"], data["valorparcela"], data["data_pagamento"] = \
                Valor_pagar(data["valor"], data["qtd_parcela"])

            data['telefone'] = validar_telefone(data['telefone'])
            data['cpf'] = validar_cpf(data['cpf'])
            gera_pdf(data)
            pdf_base64 = base64.b64encode(open('D:/brq/emprestimo/arquivo.pdf', 'rb').read())
            return {'status_code': 200, "message": "Sucess", "data": pdf_base64}
        else:
            print('dados invalidos')
    except KeyError as e:
        message = "Parametros invalidos: {}".format(e)
        return {"status_code": 400, "message": message}


if __name__ == '__main__':
    payload = {
        "body": {
            "nome": "Bruno de Almeida",
            "email": "brunodealmeida17@hotmail.com",
            "telefone": "61993069676",
            "cpf": "04352598144",
            "valor": 5000.0,
            "qtd_parcela": 10
        }
    }
    retorno = lambda_handler(
        payload,
        None
    )
    print(retorno)
