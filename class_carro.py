class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0 
    
    def mostrar_dados(self):
        print(f"Carro: {self.marca} {self.modelo} \nAno: {self.ano}")
        print(f"Velocidade agora: {self.velocidade} Km/h")

    def acelerar(self):
        self.velocidade += 10
        print("Voce Acelerou 10 Km/h")
    
    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        else:
            self.velocidade = 0 
            print("Voce freiou")

car1 = Carro("Chevrolet", "Onix", 2020)

car1.mostrar_dados()
car1.acelerar()
car1.mostrar_dados()
car1.frear()
car1.mostrar_dados()
car1.frear() 