# Classe onde é passado o nome do cliente e a nota do mesmo
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota