class Vendedor:
    def __init__(self, nome, idade, peso):
        
        self.nome = nome 
        self.idade = idade
        self.peso = peso 
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg"
