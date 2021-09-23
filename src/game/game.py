class Game(object):

    def __init__(self):
        self._players = []
        self._pending_actions = []

    def add_player(self, player):
        self._players.append(player)

    def setup_game(self):
        raise NotImplementedError("setup_game is not implemented")

    def get_next_player(self):
        return self._pending_actions.pop(0).player

    def get_game_state(self):
        raise NotImplementedError("get_game_state is not implemented")