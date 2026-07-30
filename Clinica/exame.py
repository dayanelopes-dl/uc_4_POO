class Exame:
    def __init__(self, nome, data, resultado):
        self.nome = nome
        self.data = data
        self.resultado = resultado
        self.status = "Pendente"

    def exibir_dados(self):
        print("\n--- DADOS DO EXAME ---")
        print(f"Nome: {self.nome}")
        print(f"Data: {self.data}")
        print(f"Resultado: {self.resultado}")
        print(f"Status: {self.status}")
        
