class Funcionario:
    def __init__(self, cod, nome, salario):
        self.cod = cod
        self.nome = nome
        self.__salario = salario
        self.historico_salarios = []

    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.__salario = self.__salario + self.__salario * (percentual / 100)
            self.historico_salarios.append(percentual)
            self.historico_salarios.append(self.__salario)

        return self.historico_salarios

    def exibir_informacoes(self):
        print(
            f"O funcionário {self.nome} de código {self.cod} possui um salário atual de {self.__salario} reais. Seu histório de aumento salarial é: {self.historico_salarios}")


if __name__ == "__main__":
    funcionario1 = Funcionario(1, "Julia", 3000)
    funcionario1.exibir_informacoes()
    funcionario1.aumentar_salario(10)
    funcionario1.exibir_informacoes()