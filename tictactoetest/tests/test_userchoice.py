from unittest.mock import patch
from tictactoetest import __version__
from tictactoetest.tictactoe import user_choice


def test_version():
    assert __version__ == "0.1.0"


@patch("builtins.input", return_value="5")
def test_choice_firstsuccessX(mock_input):
    """Should return as player 2's turn and spot 5 on the board filled in with an X"""
    isplayer1_in = True
    board_in = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    player1choice = user_choice(isplayer1_in, board_in, "X", "O")

    isplayer1_out = False
    board_out = ["-", "-", "-", "-", "-", "X", "-", "-", "-"]
    assert player1choice == (isplayer1_out, board_out)


@patch("builtins.input", return_value="8")
def test_choice_lastsuccessO(mock_input):
    """Should return as player 1's turn and whole board filled with Xs, except bottom right with O"""
    isplayer1_in = False
    board_in = ["X", "X", "X", "X", "X", "X", "X", "X", "-"]
    player1choice = user_choice(isplayer1_in, board_in, "X", "O")

    isplayer1_out = True
    board_out = ["X", "X", "X", "X", "X", "X", "X", "X", "O"]
    assert player1choice == (isplayer1_out, board_out)


@patch("builtins.input", side_effect=["3", "10", "0"])
def test_choice_multipleattempt1(mock_input):
    """Should return as player 1's turn, should not work when spot 3 is taken on the board, and not 10 as it is out of range of 0-8. Final try of spot 0 should be successful"""
    isplayer1_in = False
    board_in = ["-", "X", "O", "O", "X", "O", "X", "-", "X"]
    player1choice = user_choice(isplayer1_in, board_in, "X", "O")

    isplayer1_out = True
    board_out = ["O", "X", "O", "O", "X", "O", "X", "-", "X"]
    assert player1choice == (isplayer1_out, board_out)


@patch("builtins.input", side_effect=["T", "2"])
def test_choice_multipleattempt2(mock_input):
    """Should return as player 1's turn, and should not accept T as an input, then accepts 2 as a second attempt"""
    isplayer1_in = False
    board_in = ["-", "-", "-", "-", "-", "-", "-", "X", "-"]
    player1choice = user_choice(isplayer1_in, board_in, "X", "O")

    isplayer1_out = True
    board_out = ["-", "-", "O", "-", "-", "-", "-", "X", "-"]
    assert player1choice == (isplayer1_out, board_out)
