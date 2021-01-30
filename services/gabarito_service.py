import csv

from data.models.gabarito_model import GabaritoModel


def persistir_gabarito(data: GabaritoModel) -> None:
    with open('arquivos/gabaritos.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data.__dict__.values())
