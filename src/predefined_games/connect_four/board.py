import numpy as np

class ConnectFourBoard(object):

    def __init__(self, row_count=6, col_count=7):
        self._row_count = row_count
        self._col_count = col_count
        self._board = np.full([row_count, col_count], 0)

    @property
    def row_count(self):
        return self._row_count

    @property
    def col_count(self):
        return self.col_count

    def print_board(self):
        print(self._board)

    def get_symbols(self):
        return np.unique(self._board)

    def lowest_open_row(self, col):
        open_rows = np.where(col!=0)[0]
        if len(open_rows) == 0:
            open_row_idx = self._row_count
        else:
            open_row_idx = open_rows[0]
        return open_row_idx - 1

    def add_disc(self, id, col_num):
        col = self._board[:,col_num]
        open_row_idx = self.lowest_open_row(col)
        col[open_row_idx] = id

    def get_open_columns(self):
        return np.where(self._board[0] == 0)[0].tolist()

    def _check_board_winner(self, board):
        vals = list(np.unique(board))
        if 0 in vals:
            vals.remove(0)

        for val in vals:
            locations = np.where(board == val)
            list_of_coords = list(zip(locations[0], locations[1]))
            list_of_coords.sort(key=lambda t: (-t[0], t[1]))

            has_won = False

            for (x, y) in list_of_coords:
                if x <= self._col_count - 3:
                    # Check horizontal
                    if set([(x, y), (x+1, y), (x+2, y), (x+3, y)]).issubset(list_of_coords):
                        has_won = True
                    elif set([(x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)]).issubset(list_of_coords):
                        has_won = True
                    elif set([(x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)]).issubset(list_of_coords):
                        has_won = True
                if y <= self._row_count - 3:
                    if set([(x, y), (x, y+1), (x, y+2), (x, y+3)]).issubset(list_of_coords):
                        has_won = True

                if has_won:
                    return val

        return 0

    def has_winner(self):
        return self._check_board_winner(self._board)

    def has_stalemate(self):
        symbols = list(np.unique(self._board))
        if 0 in symbols:
            symbols.remove(0)

        for symbol in symbols:
            best_board = np.where(self._board == 0, symbol, self._board)

            if self._check_board_winner(best_board) != 0:
                return False

        return True

    def to_array(self):
        pass
