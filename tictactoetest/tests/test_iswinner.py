from tictactoetest import __version__
from tictactoetest.tictactoe import is_winner


def test_version():
    assert __version__ == "0.1.0"


def test_win_gamestart():
    """Game should not be over on game start"""
    assert is_winner(["-", "-", "-", "-", "-", "-", "-", "-", "-"], True) is False


def test_win_diagonal():
    """Game should be over with diagonal win"""
    assert is_winner(["X", "-", "O", "-", "X", "O", "-", "-", "X"], True) is True


def test_win_draw():
    """Game should be over with a full board (draw)"""
    assert is_winner(["X", "O", "O", "O", "X", "X", "X", "O", "O"], True) is True


def test_win_nowin():
    """Game should not be over without a winner"""
    assert is_winner(["O", "X", "O", "-", "O", "O", "-", "X", "X"], False) is False


def test_win_horizontal():
    """Game should be over with horizontal win"""
    assert is_winner(["X", "X", "X", "X", "O", "O", "O", "O", "X"], False) is True


def test_win_vertical():
    """Game should be over with vertical win"""
    assert is_winner(["O", "X", "X", "O", "O", "X", "-", "-", "X"], False) is True


def test_win_o():
    """Game should be over when O wins"""
    assert is_winner(["O", "O", "O", "-", "X", "O", "-", "X", "X"], False) is True
