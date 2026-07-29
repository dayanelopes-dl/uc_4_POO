class Funcionario():
    def __init__(self, matricula , nome, cargo , salario):
        self.matricula = matricula
        self.nome = nome 
        self.cargo = cargo 
        self.salario = salario

    def exibir_dados(self):
        print("\n Dados")
        print(f"Matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")

    def alterar_cargo(self, novo_cargo):
        self.cargo = novo_cargo
        print(f"Cargo alterado: {novo_cargo}")

    def aplicar_reajuste(self,percentual):
        aumento = self.salario * percentual/100
        self.salario += aumento
        print(f"salario ajustado: {aumento}")


funcionario = Funcionario("00101", "João", "TI", 1000)

funcionario.exibir_dados()
funcionario.alterar_cargo("Ass.financeiro")

funcionario.aplicar_reajuste(10)
funcionario.exibir_dados()
