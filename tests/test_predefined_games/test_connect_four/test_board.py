from src.predefined_games.connect_four import ConnectFourBoard

def test_board_creation():

    board = ConnectFourBoard()

    assert board.get_symbols() == [' ']

def test_board_has_win_vert_1():

    board = ConnectFourBoard()

    board.add_disc('x', 3)
    board.add_disc('x', 3)
    board.add_disc('x', 3)
    board.add_disc('x', 3)

    assert board.has_winner() == 'x'

def test_board_has_win_vert_2():

    board = ConnectFourBoard()

    board.add_disc('x', 3)
    board.add_disc('x', 3)
    board.add_disc('o', 3)
    board.add_disc('o', 3)
    board.add_disc('o', 3)
    board.add_disc('o', 3)

    assert board.has_winner() == 'o'


def test_board_has_horiz_1():

    board = ConnectFourBoard()
    board.add_disc('x', 0)
    board.add_disc('x', 3)
    board.add_disc('x', 2)

    assert board.has_winner() == ' '

    board.add_disc('x', 1)

    assert board.has_winner() == 'x'

def test_board_has_horiz_2():

    board = ConnectFourBoard()
    board.add_disc('x', 0)
    board.add_disc('x', 3)
    board.add_disc('x', 2)

    assert board.has_winner() == ' '

    board.add_disc('o', 1)

    print(board._board)

    assert board.has_winner() == ' '

    board.add_disc('x', 4)
    board.add_disc('x', 6)

    assert board.has_winner() == ' '

    board.add_disc('x', 5)

    assert board.has_winner() == 'x'

def test_board_has_diag_1():

    board = ConnectFourBoard()
    board.add_disc('o', 0)
    board.add_disc('x', 1)
    board.add_disc('o', 1)
    board.add_disc('x', 2)
    board.add_disc('x', 2)
    board.add_disc('o', 2)
    board.add_disc('x', 3)
    board.add_disc('x', 3)
    board.add_disc('o', 3)
    assert board.has_winner() == ' '
    board.add_disc('o', 3)
    assert board.has_winner() == 'o'

def test_board_has_diag_2():

    board = ConnectFourBoard()
    board.add_disc('o', 0)
    board.add_disc('o', 0)
    board.add_disc('o', 0)
    board.add_disc('x', 0)
    board.add_disc('o', 1)
    board.add_disc('o', 1)
    board.add_disc('x', 1)
    assert board.has_winner() == ' '
    board.add_disc('o', 2)
    board.add_disc('x', 2)
    board.add_disc('x', 3)
    assert board.has_winner() == 'x'

def test_stalemate():
    board = ConnectFourBoard()

    board.add_disc('o', 0)
    board.add_disc('x', 0)
    board.add_disc('o', 0)
    board.add_disc('x', 0)
    board.add_disc('o', 0)
    board.add_disc('x', 0)

    board.add_disc('x', 1)
    board.add_disc('o', 1)
    board.add_disc('x', 1)
    board.add_disc('o', 1)
    board.add_disc('x', 1)
    board.add_disc('o', 1)

    board.add_disc('o', 2)
    board.add_disc('x', 2)
    board.add_disc('o', 2)
    board.add_disc('x', 2)
    board.add_disc('o', 2)
    board.add_disc('x', 2)

    board.add_disc('o', 3)
    board.add_disc('x', 3)
    board.add_disc('o', 3)
    board.add_disc('x', 3)
    board.add_disc('o', 3)
    board.add_disc('x', 3)

    board.add_disc('o', 4)
    board.add_disc('x', 4)
    board.add_disc('o', 4)
    board.add_disc('x', 4)
    board.add_disc('o', 4)
    board.add_disc('x', 4)

    board.add_disc('x', 5)
    board.add_disc('o', 5)
    board.add_disc('x', 5)
    board.add_disc('o', 5)
    board.add_disc('x', 5)
    board.add_disc('o', 5)

    board.add_disc('o', 6)
    board.add_disc('x', 6)
    board.add_disc('o', 6)
    board.add_disc('x', 6)
    board.add_disc('o', 6)
    board.add_disc('x', 6)

    assert board.has_stalemate()
