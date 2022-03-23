from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def gera_pdf(data):
    try:
        nome_pdf = "arquivo"
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf), pagesize=letter)
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica', 12)



        pdf.drawString(30, 700, 'Task de desenvolvimento em Python')
        pdf.drawString(30, 685, 'Projeto simulador de emprestimo')
        pdf.drawString(450, 700, "{}".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
        pdf.line(440, 697, 580, 697)

        pdf.drawString(30, 653, 'Nome do solicitante:')
        pdf.line(159, 650, 580, 650)
        pdf.drawString(160, 653, "{}".format(data['nome']))

        pdf.drawString(30, 633, 'Melhor E-mail:')
        pdf.line(159, 630, 580, 630)
        pdf.drawString(160, 633, "{}".format(data['email']))

        pdf.drawString(30, 613, 'Telefone do contato')
        pdf.line(159, 610, 580, 610)
        pdf.drawString(160, 613, "{}".format(data['telefone']))

        pdf.drawString(30, 593, 'CPF do solicitante:')
        pdf.line(159, 590, 580, 590)
        pdf.drawString(160, 593, "{}".format(data['cpf']))

        pdf.drawString(310, 675, 'Valor Solicitado:')
        pdf.drawString(405, 675, "R$ {:.2f}".format(data['valor']))
        pdf.line(400, 673, 580, 673)

        pdf.drawString(30, 573, 'Valor a ser pago:')
        pdf.line(159, 570, 580, 570)
        pdf.drawString(160, 573, "R$ {:.2f}" .format(data['valorTotal']))

        pdf.drawString(30, 553, 'Valor da parcela:')
        pdf.line(159, 550, 580, 550)
        pdf.drawString(160, 553, "R$ {:.2f}".format(data['valorparcela']))

        pdf.drawString(30, 533, 'Quantidade de parcela:')
        pdf.line(159, 530, 580, 530)
        pdf.drawString(160, 533, "{}x".format(data['qtd_parcela']))

        pdf.drawString(30, 513, 'Vencimento 1e parcela:')
        pdf.line(159, 510, 580, 510)
        pdf.drawString(160, 513, "{}".format(data['data_pagamento']))

        pdf.drawString(30, 493, 'Juros cobrados:')
        pdf.line(159, 490, 580, 490)
        pdf.drawString(160, 493, "R$ {:.2f}".format(data['juros']))

        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))
