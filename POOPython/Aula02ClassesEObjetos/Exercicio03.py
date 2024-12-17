"""Crie uma classe Estudante com atributos nome, nota1 e nota2.

Crie um método media() que retorna a média das duas notas do aluno.
Crie outro método situacao() que imprime "Aprovado" se a média for >= 7.0 e "Reprovado" caso contrário.
Crie alguns objetos para testar esse comportamento."""

class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2
    
    def situacao(self):
        media = self.media()
        if media >= 7:
            print("Aprovado")
        else:
            ("Reprovado")

aluno1 = Estudante("Julio", 7, 8)
aluno1.media()
aluno1.situacao()
        