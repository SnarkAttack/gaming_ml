import numpy as np
from operator import attrgetter

class MCTSNode(object):

    def __init__(self, game, parent=None, c=2):

        self._game = game
        self._parent = parent
        self._children = []
        self._visits = 0
        self._value = 0
        # c is a constant value that can be tweaked to weight
        # how important visits are compared to value
        self._c = c

    @property
    def game(self):
        return self._game

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    @property
    def visits(self):
        return self._visits

    @property
    def value(self):
        return self._value

    @property
    def childless(self):
        return len(self._children) == 0

    @property
    def unvisited(self):
        return self._visits == 0

    @property
    def has_parent(self):
        return self._parent is not None

    @property
    def ucb(self):
        return self._value + self._c * np.sqrt(np.log(self.parent.visits)/self.visits)

    def expand(self):
        pass

    def get_promising_child(self):
        """
        Return the child that maximized the upper confidence bound (UCB)
        """
        return max(self.children, key=attrgetter('ucb'))

    def backprop(self, value):
        self._value += value
        self._visits += 1


class MCTS(object):

    def __init__(self, game, num_iterations=100):

        self._root = MCTSNode(game)

        for i in range(num_iterations):
            self._step()

    @property
    def root(self):
        return self._root

    def _step(self):

        node = self.root

        while not node.childless:
            node = node.get_promising_child()

        if node.unvisited:
            # Get network value from game state here
            value = 0
        else:
            node.expand()
            node = node.get_promising_child()
            # Get network value here
            value = 0

        while node.has_parent:
            node.backprop(value)
            node = node.parent

