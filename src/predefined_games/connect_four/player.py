from src.game.player import Player
from src.game.utilities import HUMAN_CODE, COMPUTER_CODE
from .action import PlaceDiscAction

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

    def get_next_move(self):
        if self.code == HUMAN_CODE:
            choice = None
            available_columns = self._game.get_valid_columns()
            print(f"Player {self.symbol}, what column would you like to play in?\n")
            while choice not in available_columns:
                try:
                    choice = int(input(f"Select from the following list: {available_columns}\t"))
                except Exception:
                    print("Invalid input")
            game_state = self._game.perform_action(PlaceDiscAction(self, choice))
            return game_state

    def _get_valid_moves(self):
        available_columns = self._game.get_valid_columns()
        return [PlaceDiscAction(self, col) for col in available_columns]
