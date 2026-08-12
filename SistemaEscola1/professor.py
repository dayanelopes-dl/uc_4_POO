from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.__disciplina = disciplina

    def apresentar(self):
        print("\n--- DADOS DO PROFESSOR ---")
        print(f"Nome: {self.get_nome()}")
        print(f"Idade: {self.get_idade()}")
        print(f"Disciplina: {self.__disciplina}")

    def dar_aula(self):
        print(
            f"O professor {self.get_nome()} está dando aula de "
            f"{self.__disciplina}."
        )
