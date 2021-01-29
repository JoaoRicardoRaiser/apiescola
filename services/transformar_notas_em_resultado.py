from typing import List

from data.models.aprovados_model import AprovadoModel
from services.buscar_notas_alunos_service import buscar_notas_alunos

APROVADO = "Aprovado"


def transformar_notas_em_resultado() -> List[AprovadoModel]:
    notas_alunos = buscar_notas_alunos()
    alunos_aprovados = []

    for aluno in notas_alunos:
        if aluno.Nota >= 7:
            alunos_aprovados.append(AprovadoModel(aluno.NomeAluno, APROVADO, aluno.Nota, aluno.NumeroProva))

    return alunos_aprovados
