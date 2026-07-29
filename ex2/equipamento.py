class Equipamento: 
    def __init__(self, patrimonio , descricao, setor, situacao):
        self.patrimonio = patrimonio
        self.descricao = descricao 
        self.setor = setor
        self.situacao = situacao

    def exibir_dados(self):
        print("\n Dados Abaixo:")
        print(f"patrimonio: {self.patrimonio}")
        print(f"descrição: {self.descricao}")
        print(f"Setor: {self.setor}")
        print(f"Situção: {self.situacao}")

    def alterar_situacao(self, nova_situacao):
        self.situacao = nova_situacao
        print(f" A situação foi alterada para  {self.situacao}")
    



    def transferir_setor(self, novo_setor):
        self.setor = novo_setor
        print(f"Equipamento transferido para o setor {self.setor}")

ep1 = Equipamento("PAT-001", "notebook", "Financeiro","disponivel")  

ep2 = Equipamento("PAT- 002","Impressora","Recursos Humanos", " em manutenção")

ep1.exibir_dados() 
ep2.exibir_dados()

ep1.alterar_situacao("não disponivel")

ep2.transferir_setor("diretoria")
ep2.alterar_situacao("disponivel")

ep1.exibir_dados()
ep2.exibir_dados()


