# Importação de todos os modulos
from modelos.restaurante import Restaurante
from modelos.cardapio.babida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.item_cardapio import ItemCardapio

#Exemplom de restaurante, bebida, e comida do mesmo
restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

# Adicionando a bebida e o prato em um lista
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

# Retorna a variavel com o nome do restaurante e a exibição do cardapio da mesma
def main():
    restaurante_praca.exibir_cardapio

# Definição dessa pasta como a main do programa
if __name__ == '__main__':
    main()