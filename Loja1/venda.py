class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

    def finalizar_venda(self):
        if self.quantidade <= 0:
            print("Quantidade é invalida")
            return

        if self.quantidade > self.produto.estoque:
            print("Venda não realizada. estoque insuficiente")
            return

        total = self.produto.preco * self.quantidade
        self.produto.retirar_estoque(self.quantidade)

        print("\n Venda finalizada")
        print(f"Cliente: {self.cliente.nome}")
        print(f"produto: {self.produto.descricao}")
        print(f"Quantidade: {self.quantidade}")
        print(f"total: R$ {total:2f}")