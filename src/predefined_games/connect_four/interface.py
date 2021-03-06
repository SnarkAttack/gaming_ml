from .action import PlaceDiscAction
from .game import ConnectFourGame
from .player import ConnectFourPlayer
from game.utilities import HUMAN_CODE, COMPUTER_CODE

class ConnectFourInterface(object):

    def __init__(self):
        self._game = ConnectFourGame()
        self._symbols = ['x', 'o']

    def setup_game(self, player1=None, player2=None):

        code1, symbol1 = self._get_symbol_input(player1)
        player1 = ConnectFourPlayer(code1, symbol1)

        code2, symbol2 = self._get_symbol_input(player2)
        player2 = ConnectFourPlayer(code2, symbol2)

        self._game.add_player(player1)
        self._game.add_player(player2)

    def get_next_move(self):
        self._game.print_board()

        player = self._game.get_next_player()
        return player.get_next_move()

    def _get_symbol_input(self, player_code=None):

        if player_code is None:
            code = None
            while code not in [HUMAN_CODE, COMPUTER_CODE]:
                code = input(f"Is this player a human or computer?\n"
                             f"(Enter {HUMAN_CODE} for human or {COMPUTER_CODE} for computer)\t")
        else:
            code = player_code

        if player_code == HUMAN_CODE:
            symbol = None
            while symbol not in self._symbols:
                symbol = input(f"Select a symbol from the following; [{','.join(self._symbols)}]\t")
            self._symbols.remove(symbol)

        return code, symbol


    def play_game(self):
        game_state = None
        self._game.setup_game()
        while game_state not in ['x', 'o', 's']:
            game_state = self.get_next_move()
        self._game.print_board()
        if game_state == 's':
            print("Game is a stalemate")
        else:
            print(f"Player {game_state} wins!")


