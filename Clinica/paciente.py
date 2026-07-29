class Paciente:
    def __init__(self, id ,nome , idade, cpf):
     self.id = id 
     self.nome = nome
     self.idade = idade
     self.cpf = cpf 

    def exibir_dados(self):
       print("\n Dados do Paciente")
       print(f"Id: {self.id}")
       print(f"Nome do Paciente: {self.nome}")
       print(f"Idade do Paciente: {self.idade}")
       print(f"Cpf do Paciente: {self.cpf}")