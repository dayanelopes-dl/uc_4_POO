class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []
        self.__professores = []

    def cadastrar_aluno(self, aluno):
        # REGRA DE NEGÓCIO 1:
        # O aluno precisa ter pelo menos 6 anos.
        if aluno.get_idade() < 6:
            print(
                f"O aluno {aluno.get_nome()} não pode ser matriculado. "
                "Idade mínima: 6 anos."
            )
            return

        self.__alunos.append(aluno)
        print(f"Aluno {aluno.get_nome()} matriculado com sucesso!")

    def cadastrar_professor(self, professor):
        self.__professores.append(professor)
        print(
            f"Professor {professor.get_nome()} cadastrado com sucesso!"
        )

    def listar_alunos(self):
        print("\n--- ALUNOS DA ESCOLA ---")

        if len(self.__alunos) == 0:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in self.__alunos:
            print(
                f"Nome: {aluno.get_nome()} | "
                f"Idade: {aluno.get_idade()}"
            )
