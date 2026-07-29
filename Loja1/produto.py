class Produto():
    def __init__(self, codigo, descricao, preco, estoque):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def mostra_dados(self):
        print("\nDados Exibidos:")
        print(f"Código: {self.codigo}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Estoque: {self.estoque}")

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            print("estoque foi atualizado")
        else:
            print("quantidade invalida!")

    def retirar_estoque(self, quantidade):
        if quantidade < 0:
            
            print(f"Foram retiradas {quantidade} .")
        elif quantidade > self.estoque:
            print(f"estoque insuficiente")
        else:
            print("\nproduto retirado do estoque")



