from carro import Carro
from locadora import Locadora
from vendedor import Vendedor
from endereco import Endereco



vendedor1 = Vendedor("Wander", 32 , 79)
vendedor2 = Vendedor("Gabriel", 22, 60)
vendedores = [vendedor1, vendedor2]



carro1 = Carro("Chevrolet", "Onix", 2020)
carro2 = Carro("Chevrolet", "Prisma", 2020)
carros = [carro1, carro2]



endereco = Endereco(1, "São Paulo" , 300, "Centro", "Corumbá")

locadora1 = Locadora(1, vendedores, carros,  endereco)

print(locadora1)