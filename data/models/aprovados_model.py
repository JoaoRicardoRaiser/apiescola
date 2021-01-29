class AprovadoModel:
    NomeAluno: str
    Situacao: str
    Nota: int
    Prova: int

    def __init__(self, nome_aluno: str, situacao: str, nota: int, prova: int):
        self.NomeAluno = nome_aluno
        self.Situacao = situacao
        self.Nota = nota
        self.Prova = prova
