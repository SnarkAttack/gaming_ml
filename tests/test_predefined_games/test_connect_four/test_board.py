from src.predefined_games.connect_four import ConnectFourBoard

def test_board_creation():

    board = ConnectFourBoard()

    assert board.get_symbols() == [0]

def test_board_has_win_vert_1():

    board = ConnectFourBoard()

    board.add_disc(1, 3)
    board.add_disc(1, 3)
    board.add_disc(1, 3)
    board.add_disc(1, 3)

    assert board.has_winner() == 1

def test_board_has_win_vert_2():

    board = ConnectFourBoard()

    board.add_disc(1, 3)
    board.add_disc(1, 3)
    board.add_disc(2, 3)
    board.add_disc(2, 3)
    board.add_disc(2, 3)
    board.add_disc(2, 3)

    assert board.has_winner() == 2


def test_board_has_horiz_1():

    board = ConnectFourBoard()
    board.add_disc(1, 0)
    board.add_disc(1, 3)
    board.add_disc(1, 2)

    assert board.has_winner() == 0

    board.add_disc(1, 1)

    assert board.has_winner() == 1

def test_board_has_horiz_2():

    board = ConnectFourBoard()
    board.add_disc(1, 0)
    board.add_disc(1, 3)
    board.add_disc(1, 2)

    assert board.has_winner() == 0

    board.add_disc(2, 1)

    print(board._board)

    assert board.has_winner() == 0

    board.add_disc(1, 4)
    board.add_disc(1, 6)

    assert board.has_winner() == 0

    board.add_disc(1, 5)

    assert board.has_winner() == 1

def test_board_has_diag_1():

    board = ConnectFourBoard()
    board.add_disc(2, 0)
    board.add_disc(1, 1)
    board.add_disc(2, 1)
    board.add_disc(1, 2)
    board.add_disc(1, 2)
    board.add_disc(2, 2)
    board.add_disc(1, 3)
    board.add_disc(1, 3)
    board.add_disc(2, 3)
    assert board.has_winner() == 0
    board.add_disc(2, 3)
    assert board.has_winner() == 2

def test_board_has_diag_2():

    board = ConnectFourBoard()
    board.add_disc(2, 0)
    board.add_disc(2, 0)
    board.add_disc(2, 0)
    board.add_disc(1, 0)
    board.add_disc(2, 1)
    board.add_disc(2, 1)
    board.add_disc(1, 1)
    assert board.has_winner() == 0
    board.add_disc(2, 2)
    board.add_disc(1, 2)
    board.add_disc(1, 3)
    assert board.has_winner() == 1

def test_stalemate():
    board = ConnectFourBoard()

    board.add_disc(2, 0)
    board.add_disc(1, 0)
    board.add_disc(2, 0)
    board.add_disc(1, 0)
    board.add_disc(2, 0)
    board.add_disc(1, 0)

    board.add_disc(1, 1)
    board.add_disc(2, 1)
    board.add_disc(1, 1)
    board.add_disc(2, 1)
    board.add_disc(1, 1)
    board.add_disc(2, 1)

    board.add_disc(2, 2)
    board.add_disc(1, 2)
    board.add_disc(2, 2)
    board.add_disc(1, 2)
    board.add_disc(2, 2)
    board.add_disc(1, 2)

    board.add_disc(2, 3)
    board.add_disc(1, 3)
    board.add_disc(2, 3)
    board.add_disc(1, 3)
    board.add_disc(2, 3)
    board.add_disc(1, 3)

    board.add_disc(2, 4)
    board.add_disc(1, 4)
    board.add_disc(2, 4)
    board.add_disc(1, 4)
    board.add_disc(2, 4)
    board.add_disc(1, 4)

    board.add_disc(1, 5)
    board.add_disc(2, 5)
    board.add_disc(1, 5)
    board.add_disc(2, 5)
    board.add_disc(1, 5)
    board.add_disc(2, 5)

    board.add_disc(2, 6)
    board.add_disc(1, 6)
    board.add_disc(2, 6)
    board.add_disc(1, 6)
    board.add_disc(2, 6)
    board.add_disc(1, 6)

    assert board.has_stalemate()
