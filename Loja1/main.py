from produto import Produto
from cliente import Cliente
from venda import Venda


def main():
    cliente1 = Cliente(
        1,
        "João",
        "123.456.789-00")
    
    produto1 = Produto("CAM-006", 
                    "Camisa Unissex",
                        49.50,
                        10)
    venda1 = Venda(
        cliente1,
        produto1,
        2
    )

    cliente1.exibir_dados()
    produto1.mostra_dados()

    venda1.finalizar_venda()
    

if __name__ == "__main__":
    main()