from .defines import STALEMATE
from ...game import Game, PendingAction
from .action import PlaceDiscAction
from .board import ConnectFourBoard

class ConnectFourGame(Game):

    def __init__(self, row_count=6, col_count=7):
        super().__init__()
        self._game_board = ConnectFourBoard(row_count, col_count)

    def setup_game(self):
        for player in self._players:
            self._pending_actions.append(PendingAction(player))

    def add_player(self, player):
        super().add_player(player)
        self.id = len(self._players)

    def perform_action(self, action):
        if isinstance(action, PlaceDiscAction):
            self._game_board.add_disc(action.player.symbol, action.column)
            self._pending_actions.append(PendingAction(action.player))
        return self.get_game_state()

    def get_valid_columns(self):
        return self._game_board.get_open_columns()

    def print_board(self):
        self._game_board.print_board()

    def get_game_state(self):
        """
        Valid states:
        0 for game continuation
        player id for player having achieved a victory
        -1 for a stalemate
        """
        if self._game_board.has_stalemate():
            return STALEMATE
        elif state := self._game_board.has_winner():
            return state
        else:
            return 0