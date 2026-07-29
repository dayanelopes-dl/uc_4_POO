class Produto():
    def __init__(self, codigo, descricao, preco, quantidade):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def mostra_dados(self):
        print("\nDados Exibidos:")
        print(f"Código: {self.codigo}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def calcular_estoque(self):
        total_estoque = self.quantidade * self.preco
        print(f"Valor total do estoque: R$ {total_estoque:.2f}")

    def adicionar_unidade(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade
            print("estoque foi atualizado")
        else:
            print("quantidade invalida!")

    def retirar_unidade(self, quantidade):
        if quantidade < 0:
            
            print(f"Foram retiradas {quantidade} .")
        elif quantidade > self.quantidade:
            print(f"estoque insuficiente")
        else:
            print("\nproduto retirado do estoque")



