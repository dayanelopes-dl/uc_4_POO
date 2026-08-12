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


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

escola = Escola("Escola Futuro")

# Criando alunos
aluno1 = Aluno("João", 15, "A001")
aluno2 = Aluno("Maria", 16, "A002")
aluno3 = Aluno("Pedro", 5, "A003")

# Criando professor
professor1 = Professor("Carlos", 35, "Programação")

# Cadastrando alunos
escola.cadastrar_aluno(aluno1)
escola.cadastrar_aluno(aluno2)
escola.cadastrar_aluno(aluno3)

# Cadastrando professor
escola.cadastrar_professor(professor1)

# Adicionando notas
print("\n--- NOTAS DO JOÃO ---")
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(9)

print("\n--- NOTAS DA MARIA ---")
aluno2.adicionar_nota(5)
aluno2.adicionar_nota(6)
aluno2.adicionar_nota(4)

# Mostrando dados
aluno1.mostrar_dados()
aluno2.mostrar_dados()

# Professor dando aula
professor1.apresentar()
professor1.dar_aula()

# Listando alunos
escola.listar_alunos()
