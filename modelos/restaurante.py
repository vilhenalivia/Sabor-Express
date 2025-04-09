#Importação das pastas
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

#Classe do restaurante
class Restaurante:

    #Lista vazia para adicionar os restaurantes criados
    restaurantes = []

    """
    Construtor onde é definido o nome do restaurante, categoria do mesmo e a ativação dele onde começa contabilizando como Falso, ou seja, não ativo.
    Criação de duas listas sendo elas de avaliação gerada pelo cliente e cardapio onde é alocado os cardápios disponiveis
    Após toda essas definições o novo restaurante é alocado na lista de Restaurantes definida anteriormente
    """
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    # Fução que retorna o nome e a categoria do restaurante em forma de texto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    """
    Usando decorator classmethod para executar o método sem a classe ser instanciada.
    Método que lista:
    - Nome do restaurante 
    - Categoria do restaurante
    - Média de avaliações do restaurante
    - Status do restaurante
    """
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    """
    Propriedade da classe para gerenciar os atributos protegidos da classe
    Atrubuto: Ativo 
    retoorna se o restaurante estáativo ou não
    """
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    # Método de alternar estado onde transforma o atributo ativo em não ativo
    def alternar_estado(self):
        self._ativo = not self._ativo

    """ 
    Método de receber avaliação. Tem como parametro o cliente e a nota, se a nota estiver entre 0 á 5 o a Classe Avaliação é instaciada passando o cliente e a nota do mesmo
    Isso tudo é alocado na lista de avalição.
    """
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    """
    Propriedade onde é gerenciado o atributo da classe de modo que só pode ser lido e não editado.
    """
    @property
    def media_avaliacoes(self):
        # Verificação se possui algo na avaliação, se não, retona um "-"
        if not self._avaliacao:
            return '-'
        # Variavel que retona a a soma as notas atribuidas
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        # Variável que conta a quantidade de notas atribuidas
        quantidade_de_notas = len(self._avaliacao)
        # Caucula a média arredondada das notas
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    # Método que adiciona uma instância de Item Cardapio na lista "_cardapio"
    def adicionar_no_cardapio( self, item ):
        if isinstance(item, ItemCardapio) :
            self._cardapio.append(item)

    # Exibir itens da lista "_cardapio
    # Property pois eu só quero possibilitar a leitura
    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        # Enumerate para passar os itens de forma númerada
        for i, item in enumerate(self._cardapio, start= 1):
            # Se tiver o atributo 'descrição' imprime a mensagem do prato, se não, imprime a mensagem da bebida que não tem o atributo "descrição".
            if hasattr (item, 'descricao'):
                mensagem_prato = f'{i} - Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else: 
                mensagem_bebida = f'{i} - Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tamanho}'          
                print(mensagem_bebida)