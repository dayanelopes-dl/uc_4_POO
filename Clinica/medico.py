class Medico:
    def __init__(self, id, nome , crm , especialidade):
     self.id = id
     self.nome = nome
     self.crm = crm 
     self.especialidade = especialidade

    def exibir_dados(self):
     print("\n Dados do Medico")  
     print(f"Nome do Medico: {self.nome}")
     print(f"Crm: {self.crm}")
     print(f"Especidalidade: {self.especialidade}")
