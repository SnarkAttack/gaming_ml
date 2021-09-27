from ...game.action import Action

class PlaceDiscAction(Action):

    def __init__(self, player, column):
        super().__init__(player)
        self._column = column

    @property
    def column(self):
        return self._column