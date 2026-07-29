class Endereco:
    def __init__(self, id , rua , numero , bairro , cidade):
        self.id = id 
        self.rua = rua 
        self.numero = numero 
        self.bairro = bairro
        self.cidade = cidade 

    def __str__(self):
        return f"id: {self.id}, rua: {self.rua}, numero: {self.numero}, bairro: {self.bairro}, cidade: {self.cidade}"
