class AlunoNotaModel:
    NumeroProva: int
    NomeAluno: str
    Nota: int

    def __init__(self, numero_prova: int, nome_aluno: str, nota: int):
        self.NumeroProva = numero_prova
        self.NomeAluno = nome_aluno
        self.Nota = nota
