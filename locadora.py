
class Locadora:
    def __init__(self, id , vendedores, carros , endereco):
        self.id = id 
        self.vendedores = vendedores
        self.carros = carros
        self.endereco = endereco

    def __str__(self):
            texto = f"Locadora: {self.id}\n"

            texto += "Vendedores:\n"
            for vendedor in self.vendedores:
                texto += f"  {vendedor}\n"

            texto += "Carros:\n"
            for carro in self.carros:
                texto += f"  {carro}\n"

            texto += f"Endereço: {self.endereco}"

            return texto
