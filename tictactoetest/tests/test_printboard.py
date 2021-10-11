from unittest.mock import patch, call
from tictactoetest import __version__
from tictactoetest.tictactoe import print_board


def test_version():
    assert __version__ == '0.1.0'


@patch('builtins.print')
def test_correct_print_slice1(mock_print):
    '''Should print the correct board with some moves already made'''
    boardprint = print_board(['-', 'X', 'O', 'O', 'X', '-', '-', 'X', 'O'])
    assert mock_print.mock_calls == [
        call("Current board state:\n['-', 'X', 'O']\n['O', 'X', '-']\n['-', 'X', 'O']\n")]


@patch('builtins.print')
def test_correct_print_slice2(mock_print):
    '''Should print the correct board with some different moves already made'''
    boardprint = print_board(['X', '-', '-', '-', '-', '-', '-', '-', 'O'])
    assert mock_print.mock_calls == [
        call("Current board state:\n['X', '-', '-']\n['-', '-', '-']\n['-', '-', 'O']\n")]
