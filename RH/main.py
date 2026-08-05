from funcionario import Funcionario

funcionario1 = Funcionario(
    1234,
    "João",
    "Auxiliar Administrativo",
    1000
)

funcionario1.exibir_dados()

print("\n Tentando alterar o salario para negativo")
funcionario1.set_salario(-500)

print("\n Tentando alterar o salario para maior")
funcionario1.set_salario(10001)
