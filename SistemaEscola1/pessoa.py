class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
