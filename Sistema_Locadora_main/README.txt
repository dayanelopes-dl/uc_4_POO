SISTEMA DE LOCAÇÃO DE VEÍCULOS - UC4 POO COM PYTHON
===================================================

Conteúdos trabalhados:
- Classes e objetos
- Atributos e métodos
- Construtor __init__
- self
- Organização em múltiplos arquivos
- Comunicação entre objetos
- Encapsulamento
- Getters e setters
- Herança
- super()
- Sobrescrita de métodos
- Polimorfismo
- Regras de negócio
- Listas
- Estruturas condicionais
- Estruturas de repetição
- Tratamento básico de erros
- Interação com o usuário

ARQUIVOS
--------
cliente.py       -> cadastro e proteção dos dados do cliente
veiculo.py       -> classe-pai dos veículos
carro.py         -> classe filha Carro
moto.py          -> classe filha Moto
caminhonete.py   -> classe filha Caminhonete
eletrico.py      -> classe filha Eletrico
aluguel.py       -> relacionamento entre Cliente e Veiculo
main.py          -> fluxo principal e interação com o usuário

COMO EXECUTAR
-------------
1. Abra a pasta no VS Code.
2. Abra o terminal.
3. Execute:
   python main.py

   ou, no Windows:
   py main.py

POLIMORFISMO
------------
O principal exemplo está no método calcular_aluguel():

- Carro: 5% de desconto acima de 10 dias.
- Moto: 10% de desconto acima de 5 dias.
- Caminhonete: taxa fixa de seguro de R$ 150.
- Elétrico: desconto ecológico de 15%.

A classe Aluguel não precisa saber qual é o tipo do veículo.
Ela apenas executa:

self.veiculo.calcular_aluguel(...)

O Python utiliza automaticamente o método correspondente ao tipo
real do objeto.
