
class Game:
    def __init__(self,nome,categoria,console):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._console = console.title()

    def __str__(self):
        return f'Nome do Jogo: {self._nome} | Categoria do Jogo: {self._categoria} | Console do Jogo: {self._console}'