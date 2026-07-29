class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

    def finalizar_venda(self):
        if self.quantidade <= 0:
            print("Quantidade é invalida")
            return

        if self.quantidade > self.produto.quantidade:
            print("Venda não realizada. estoque insuficiente")
            return

        total = self.produto.preco * self.quantidade
        self.produto.retirar_unidade(self.quantidade)

        print("\n Venda finalizada")
        print(f"Cliente: {self.cliente.nome}")
        print(f"produto: {self.produto.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"total: R$ {total:2f}")