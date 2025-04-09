from modelos.cardapio.item_cardapio import ItemCardapio

"""
Classe que herda da classe ItemCardápio
É passado o nome do item o preço importados da classe ItemCardapio e a descrição criada propriamente para a classe Prato
"""
class Prato(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao 

    def __str__(self):
        return self._nome
    
    # Possui a aplicação de desconto do método abstrato
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
        