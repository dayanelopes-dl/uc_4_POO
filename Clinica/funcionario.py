class Funcionario:
    def __init__(self, codigo, nome, cargo):
        self.codigo = codigo
        self.nome = nome
        self.cargo = cargo

    def exibir_dados(self):
        print("\n--- DADOS DO FUNCIONÁRIO ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")