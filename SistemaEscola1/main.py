from aluno import Aluno
from professor import Professor
from escola import Escola


# Criando a escola
escola = Escola("Escola Futuro")


# Criando os alunos
aluno1 = Aluno("João", 15, "A001")
aluno2 = Aluno("Maria", 16, "A002")
aluno3 = Aluno("Pedro", 5, "A003")


# Criando o professor
professor1 = Professor(
    "Carlos",
    35,
    "Programação"
)


# Cadastrando os alunos
print("\n--- CADASTRO DE ALUNOS ---")

escola.cadastrar_aluno(aluno1)
escola.cadastrar_aluno(aluno2)
escola.cadastrar_aluno(aluno3)


# Cadastrando o professor
print("\n--- CADASTRO DE PROFESSOR ---")

escola.cadastrar_professor(professor1)


# Adicionando notas do João
print("\n--- NOTAS DO JOÃO ---")

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7)
aluno1.adicionar_nota(9)


# Adicionando notas da Maria
print("\n--- NOTAS DA MARIA ---")

aluno2.adicionar_nota(5)
aluno2.adicionar_nota(6)
aluno2.adicionar_nota(4)


# Mostrando dados dos alunos
aluno1.mostrar_dados()
aluno2.mostrar_dados()


# Mostrando dados do professor
professor1.apresentar()
professor1.dar_aula()


# Listando alunos
escola.listar_alunos()
