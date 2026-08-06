from paciente import Paciente
from medico import Medico

paciente1 = Paciente(
    "Luiz",
    "123.456.789-00",
    "(67)9999-4545",
    "America",
    20,
    "Unimed"
)

medico1 = Medico(
    "João",
    "111.222.333-66",
    "(67)98282-6161",
    "Frei Mariano",
    "01020304",
    "Clinico Geral"
)

print("Paciente")
paciente1.exibir_paciente()

print("Medico")
medico1.exibir_medico()