class Cliente:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo #Publico
        self.__nome = nome #Privado
        self.__cpf = cpf #Privado

        #Setters para validar dados recebidos
        self.set_nome(nome)
        self.set_cpf(cpf)

    def get_nome(self):
        #Retorna o nome do cliente
        return self.__nome
    
    def set_nome(self, nome):
        #Altera o nome do cliente
        nome = nome.strip()

        if len(nome) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False
        
        self.__nome = nome
        return True
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        cpf_limpo = cpf.replace(".", "").replace("-", "").strip()

        if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
            print("Erro: o CPF deve possuir exatamente 11 numeros.")
            return False
        
        self.__cpf = cpf_limpo
        return True
    
    def exibir_dados(self):
        print("\n--- DADOS DO CLIENTE ---")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.__nome}")
        print(f"Cpf: {self.__cpf}")
    
        