from abc import ABC, abstractclassmethod

"""
Classe item cardápio onde é passado o nome do item e o preço
"""
class ItemCardapio(ABC):
    # Construtor
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    
    # Classe abstrata que aplica descontos em obrigatoriamente em todas as classes derivadas da classe abstrata, ou seja, Classe 'ItemCardapio'
    @abstractclassmethod
    def aplicar_desconto(self):
        pass
        