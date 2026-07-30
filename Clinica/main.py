from paciente import Paciente
from medico import Medico
from consulta import Consulta
from exame import Exame
from receita import Receita
from funcionario import Funcionario

def main():

    pacientes = []
    medicos = []
    consultas = []
    exames = []
    receitas = []
    funcionarios = []

    while True:

        print("\n========== CLÍNICA ==========")
        print("1 - Cadastrar Paciente")
        print("2 - Cadastrar Médico")
        print("3 - Cadastrar Funcionário")
        print("4 - Agendar Consulta")
        print("5 - Listar Consultas")
        print("6 - Histórico do Paciente")
        print("7 - Cadastrar Exame")
        print("8 - Cadastrar Receita")
        print("9 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:

            codigo = int(input("Código: "))
            nome = input("Nome: ")
            cpf = input("CPF: ")
            idade = int(input("Idade: "))

            paciente = Paciente(codigo, nome, cpf, idade)
            paciente.historico = []

            pacientes.append(paciente)

            print("Paciente cadastrado!")

        elif opcao == 2:

            codigo = int(input("Código: "))
            nome = input("Nome: ")
            crm = input("CRM: ")
            especialidade = input("Especialidade: ")

            medico = Medico(codigo, nome, crm, especialidade)
            medicos.append(medico)

            print("Médico cadastrado!")

        elif opcao == 3:

            codigo = int(input("Código: "))
            nome = input("Nome: ")
            cargo = input("Cargo: ")

            funcionario = Funcionario(codigo, nome, cargo)
            funcionarios.append(funcionario)

            print("Funcionário cadastrado!")

        elif opcao == 4:

            if len(pacientes) == 0 or len(medicos) == 0:
                print("Cadastre um paciente e um médico primeiro.")
                continue

            print("\nPACIENTES")
            for paciente in pacientes:
                print(paciente.codigo, "-", paciente.nome)

            codPaciente = int(input("Código do paciente: "))

            pacienteEscolhido = None

            for paciente in pacientes:
                if paciente.codigo == codPaciente:
                    pacienteEscolhido = paciente

            print("\nMÉDICOS")
            for medico in medicos:
                print(medico.codigo, "-", medico.nome)

            codMedico = int(input("Código do médico: "))

            medicoEscolhido = None

            for medico in medicos:
                if medico.codigo == codMedico:
                    medicoEscolhido = medico

            codigo = int(input("Código da consulta: "))
            data = input("Data: ")
            horario = input("Horário: ")
            valor = float(input("Valor da consulta: R$ "))
            classificacao = input("Classificação: ")

            ocupado = False

            for consulta in consultas:
                if consulta.medico.codigo == codMedico and consulta.data == data and consulta.horario == horario:
                    ocupado = True

            if ocupado:
                print("Já existe uma consulta nesse horário.")
            else:

                consulta = Consulta(
                    codigo,
                    pacienteEscolhido,
                    medicoEscolhido,
                    data,
                    horario
                )

                consulta.valor = valor
                consulta.classificacao = classificacao

                consultas.append(consulta)
                pacienteEscolhido.historico.append(consulta)

                print("Consulta cadastrada com sucesso!")

        elif opcao == 5:

            print("\nCONSULTAS AGENDADAS")

            for consulta in consultas:
                consulta.exibir_dados()
                print("Valor: R$", consulta.valor)
                print("Classificação:", consulta.classificacao)

        elif opcao == 6:

            codigo = int(input("Código do paciente: "))

            for paciente in pacientes:

                if paciente.codigo == codigo:

                    print("\nHistórico de Consultas")

                    if len(paciente.historico) == 0:
                        print("Nenhuma consulta encontrada.")
                    else:
                        for consulta in paciente.historico:
                            consulta.exibir_dados()

        elif opcao == 7:

            codigo = int(input("Código do exame: "))
            nome = input("Nome do exame: ")
            data = input("Data: ")
            resultado = input("Resultado: ")

            exame = Exame(codigo, nome, data, resultado)

            exames.append(exame)

            print("Exame cadastrado!")

        elif opcao == 8:

            codigo = int(input("Código da receita: "))
            medicamento = input("Medicamento: ")
            dosagem = input("Dosagem: ")
            observacao = input("Observação: ")

            receita = Receita(codigo, medicamento, dosagem, observacao)

            receitas.append(receita)

            print("Receita cadastrada!")

        elif opcao == 9:
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()