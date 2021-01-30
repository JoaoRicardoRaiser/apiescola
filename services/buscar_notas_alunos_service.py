import csv
from typing import List

from data.models.aluno_nota_model import AlunoNotaModel
from data.models.gabarito_model import GabaritoModel
from data.models.resposta_model import RespostaModel


def buscar_notas_alunos() -> List[AlunoNotaModel]:
    csv_respostas = open('arquivos/respostas.csv')
    leitor_csv_respostas = csv.DictReader(csv_respostas, delimiter=';')
    lista_respostas = []
    for linha in leitor_csv_respostas:
        lista_respostas.append(
            RespostaModel(
                linha["NomeAluno"],
                int(linha["NumeroProva"]),
                linha["Questao1"],
                linha["Questao2"],
                linha["Questao3"],
                linha["Questao4"],
                linha["Questao5"]
            )
        )

    csv_gabaritos = open('arquivos/gabaritos.csv')
    leitor_csv_gabaritos = csv.DictReader(csv_gabaritos, delimiter=';')
    lista_gabaritos = {}
    for linha in leitor_csv_gabaritos:
        lista_gabaritos.update(
            {
                f"Prova{linha['NumeroProva']}": GabaritoModel(
                    int(linha["NumeroProva"]),
                    linha["Questao1"],
                    linha["Questao2"],
                    linha["Questao3"],
                    linha["Questao4"],
                    linha["Questao5"]
                )
            }
        )
    lista_aluno_notas = []
    for resposta in lista_respostas:
        gabarito = lista_gabaritos[f"Prova{resposta.NumeroProva}"]
        aluno_nota = calcula_nota(gabarito, resposta)
        lista_aluno_notas.append(aluno_nota)

    return lista_aluno_notas


def calcula_nota(gabarito: GabaritoModel, resposta: RespostaModel) -> AlunoNotaModel:
    nota = 0
    quantidade_respostas = 6
    for i in range(1, quantidade_respostas):
        if eval(f"resposta.Questao{i}") == eval(f"gabarito.Questao{i}"):
            nota += 2

    return AlunoNotaModel(gabarito.NumeroProva, resposta.NomeAluno, nota)
