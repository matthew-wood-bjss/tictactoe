from unittest.mock import patch, call
from tictactoetest import __version__
from tictactoetest.tictactoe import main


def test_version():
    assert __version__ == "0.1.0"


@patch("builtins.print")
@patch("builtins.input", side_effect=["O", "0", "3", "0", "1", "2", "5", "4", "8", "6"])
def test_setup_TandX2(mock_input, mock_print):
    """Test a whole playthrough of tictactoe, player 2 should win the game as X"""
    main()
    assert mock_print.mock_calls == [
        call(
            "Current board state:\n['-', '-', '-']\n['-', '-', '-']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', '-', '-']\n['-', '-', '-']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', '-', '-']\n['X', '-', '-']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', 'O', '-']\n['X', '-', '-']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', 'O', 'X']\n['X', '-', '-']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', 'O', 'X']\n['X', '-', 'O']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', 'O', 'X']\n['X', 'X', 'O']\n['-', '-', '-']\n"
        ),
        call(
            "Current board state:\n['O', 'O', 'X']\n['X', 'X', 'O']\n['-', '-', 'O']\n"
        ),
        call(
            "Current board state:\n['O', 'O', 'X']\n['X', 'X', 'O']\n['X', '-', 'O']\n"
        ),
        call("Congratulations Player 2!"),
    ]
