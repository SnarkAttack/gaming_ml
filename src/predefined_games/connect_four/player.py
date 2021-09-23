from src.game.player import Player

class ConnectFourPlayer(Player):

    def __init__(self, code, symbol):
        super().__init__()
        self._code = code
        self._symbol = symbol

    @property
    def code(self):
        return self._code

    @property
    def symbol(self):
        return self._symbol