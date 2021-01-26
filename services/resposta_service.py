import csv

from data.models.resposta_model import RespostaModel


def persistir_resposta(data: RespostaModel):
    with open('arquivos/respostas.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data.__dict__.values())
