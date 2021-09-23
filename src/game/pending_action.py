class PendingAction(object):
    
    def __init__(self, player, valid_actions=[]):
        """
        Add a pending action for a player to the turn order. In the event that
        the action is a response and the player will have limited options, the
        valid_actions parameter can be used to provide on the allowed options
        """
        self._player = player
        self._valid_actions = valid_actions
        
    @property
    def player(self):
        return self._player
    
    @property
    def valid_actions(self):
        return self._valid_actions