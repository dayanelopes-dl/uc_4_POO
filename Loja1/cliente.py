class Cliente:
    def __init__(self, codigo , nome , cpf):
        self.codigo = codigo 
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print(f"\nCliente")
        print(f"Codigo: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Cpf: {self.cpf}")