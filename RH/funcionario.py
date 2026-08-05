class Funcionario:
    def __init__(self, matricula, nome, cargo, salario):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo 
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        if novo_salario <= 1600 or novo_salario >= 10000:
            print("Erro, o salario muito baixo que o permitido")
        if novo_salario >= 1000:
            print("erro, salario muito alto")
        else:
            self.__salario = novo_salario
            print("Salario atualizado")

    def exibir_dados(self):
        print("\n --- Funcionario---")
        print(f"Matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.__salario}")
