class RespostaModel:
    NomeAluno: str
    NumeroProva: int
    Questao1: str
    Questao2: str
    Questao3: str
    Questao4: str
    Questao5: str

    def __init__(self, nome_aluno: str, numero_prova: int, questao1: str, questao2: str, questao3: str, questao4: str,
                 questao5: str):
        self.NomeAluno = nome_aluno
        self.NumeroProva = numero_prova
        self.Questao1 = questao1
        self.Questao2 = questao2
        self.Questao3 = questao3
        self.Questao4 = questao4
        self.Questao5 = questao5
