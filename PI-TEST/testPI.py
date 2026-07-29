class Usuario: 
    def __init__(self, nome, email, telefone, senha , cargo):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha 
        self.cargo = cargo
    
    def apresentar(self):
        print(f"Nome: {self.nome}. ")
        print(f"email: {self.email} ")
        print(f"telefone: {self.telefone} ")
        print(f"senha: {self.senha}" )
        print(f"cargo: {self.cargo}")

info1 = Usuario("João","joao@senac.com.br",6799243647, "Senha432","Adm")

info1.apresentar()

print("-"*40)
print("Progresso do Dia")

class Progresso:
    def __init__(self, data, aguaConsumida, pausasrealizadas, alongamentosFeitos):
        self.data = data
        self.aguaconsumida = aguaConsumida
        self.pausasrealizadas = pausasrealizadas
        self.alongamentosFeitos = alongamentosFeitos

    def mostrar_dados(self):
        print(f"Data: ", self.data)
        print(f"Agua Consumida: ", self.aguaconsumida)
        print(f"Pausas Realizadas: ", self.pausasrealizadas)
        print(f"Alongamentos Feitos: ", self.alongamentosFeitos)

p1 = Progresso("19/03/2026", "2 Litros", 1 , 4)

p1.mostrar_dados()