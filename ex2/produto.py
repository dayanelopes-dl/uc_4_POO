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
        self.quantidade += quantidade
        print(f"Foram adicionadas {quantidade} ")
        print(f"Novo estoque: {self.quantidade}")

    def retirar_unidade(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"Foram retiradas {quantidade} .")
            print(f"Novo estoque: {self.quantidade}")
        else:
            print("\nQuantidade insuficiente em estoque!")



p1 = Produto("CAM-006", "Camisa Unissex", 49.50, 1)
p2 = Produto("OCU-003", "Óculos bifocal", 100.00, 1)


p1.mostra_dados()
p1.calcular_estoque()

p2.mostra_dados()
p2.calcular_estoque()


p1.adicionar_unidade(3)
p1.retirar_unidade(2)

p2.adicionar_unidade(2)
p2.retirar_unidade(1)


print("Estoque Atualizado:")
p1.mostra_dados()
p1.calcular_estoque()

p2.mostra_dados()
p2.calcular_estoque()

