from unittest.mock import patch
from tictactoetest import __version__
from tictactoetest.tictactoe import user_setup


def test_version():
    assert __version__ == "0.1.0"


@patch("builtins.input", return_value="X")
def test_setup_X(mock_input):
    """Should return player 1 as X and player 2 as O if X is given"""
    player1choice = user_setup()
    assert player1choice == ("X", "O")


@patch("builtins.input", return_value="O")
def test_setup_O(mock_input):
    """Should return player 1 as O and player 2 as X if O is given"""
    player1choice = user_setup()
    assert player1choice == ("O", "X")


@patch("builtins.input", side_effect=["T", "X"])
def test_setup_TandX(mock_input):
    """Should return player 1 as X and player 2 as O if something other than X,x,O or o is given as an input, and then X on second attempt"""
    player1choice = user_setup()
    assert player1choice == ("X", "O")


@patch("builtins.input", side_effect=["T", "2", "o"])
def test_setup_TandX2(mock_input):
    """Should return player 1 as O and player 2 as X if numerous tries of something other than X,x,O or o is given as an input, and then O on final attempt"""
    player1choice = user_setup()
    assert player1choice == ("O", "X")
