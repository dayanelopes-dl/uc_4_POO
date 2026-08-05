from pessoa import Paciente

paciente1 = Paciente(
    1,
    'Luiz',
    '12345678900',
    20
)

print(f"\n Alterando Nome para vazio")
paciente1.set_nome("Maria")

print("Alterando cpf")
paciente1.set_cpf("999.888.777-11")

print("Alterando Idade")
paciente1.set_idade(29)



paciente1.exibir_dados()