from modelos.cardapio.item_cardapio import ItemCardapio

"""
Classe que herda do ItemCardapio
Tem como parametro o nome e o preco do item importado da classe ItemCardapio e é adicionado o atributo tamanho propriamente para a classe Bebida
"""
class Bebida(ItemCardapio):
    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome
    
    # Aplicação de desconto do metodo abstrato
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        
