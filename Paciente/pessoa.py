class Paciente: 
    def __init__(self, codigo, nome, cpf , idade):
        self.codigo = codigo
        self.__nome = nome
        self.__cpf = cpf
        self.idade = idade  

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        if nome.strip() == "":
         print("Nome Invalido")
        else:
            self.__nome = nome
            print("Nome Atualizado")

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        cpf = cpf.replace(".", "").replace(".", "")

        if len(cpf) == 11 and cpf.isdigit():
            self.cpf = cpf
            print("CPF  invalido")
    @property       # so esta colocando um apelido  
    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade Invalida")
   


    def exibir_dados(self):
        print(f"\n ---Paciente---")
        print(f"Codigo: {self.codigo}")
        print(f"Nome: {self.get_nome()}")
        print(f"Nome: {self.get_cpf()}")
        print(f"Idade: {self.get_idade()}")