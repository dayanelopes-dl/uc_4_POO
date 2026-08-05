class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome #publico
        self._idade = idade #atributo protegido, esta com () _)
        self.__peso = peso #atributo privado, esta com () __)
pessoa = Pessoa("Luiz", 30, 100)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa._idade}")
print(f"Peso: {pessoa.__peso}")
