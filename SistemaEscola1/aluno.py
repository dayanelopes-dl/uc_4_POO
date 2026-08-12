from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
            print(f"Nota {nota} adicionada.")
        else:
            print("A nota deve estar entre 0 e 10.")

    def calcular_media(self):
        if len(self.__notas) == 0:
            return 0

        return sum(self.__notas) / len(self.__notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

    def mostrar_dados(self):
        print("\n--- DADOS DO ALUNO ---")
        print(f"Nome: {self.get_nome()}")
        print(f"Idade: {self.get_idade()}")
        print(f"Matrícula: {self.__matricula}")
        print(f"Notas: {self.__notas}")
        print(f"Média: {self.calcular_media():.2f}")
        print(f"Situação: {self.verificar_aprovacao()}")
