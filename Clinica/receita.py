class Receita:
    def __init__(self, medicamento, dosagem, observacao):
        self.medicamento = medicamento
        self.dosagem = dosagem
        self.observacao = observacao

    def exibir_dados(self):
        print("\n--- DADOS DA RECEITA ---")
        print(f"Medicamento: {self.medicamento}")
        print(f"Dosagem: {self.dosagem}")
        print(f"Observação: {self.observacao}")