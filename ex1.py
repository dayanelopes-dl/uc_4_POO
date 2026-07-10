class Aluno:
    def __init__(self,nome, idade , matricula): #variavel que vai apontar para nossos atributos(guardar)
        self.nome = nome
        self.idade = idade
        self.matricula = matricula   # metado construtor

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
        print(f"Tenho {self.idade} anos.")
        print(f"A minha matricula é {self.matricula}.") #metados criados

#criamos objetos
info1 = Aluno("João",20 ,1928475)
info2 = Aluno("Maria", 19, 112233)

#chamamos metados
info1.apresentar()