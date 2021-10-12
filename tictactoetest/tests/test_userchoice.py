from unittest.mock import patch, call
from tictactoetest import __version__
from tictactoetest.tictactoe import user_choice


def test_version():
    assert __version__ == '0.1.0'


@patch('builtins.input', return_value='5')
def test_choice_firstsuccessX(mock_input):
    '''Should return as player 2's turn and spot 5 on the board filled in with an X'''
    isplayer1_in = True
    board_in = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
    player1choice = user_choice(isplayer1_in, board_in, 'X', 'O')

    isplayer1_out = False
    board_out = [
        '-', '-', '-',
        '-', '-', 'X',
        '-', '-', '-']
    assert player1choice == (isplayer1_out, board_out)


@patch('builtins.input', return_value='8')
def test_choice_lastsuccessO(mock_input):
    '''Should return as player 1's turn and whole board filled with Xs, except bottom right with O'''
    isplayer1_in = False
    board_in = [
        'X', 'X', 'X',
        'X', 'X', 'X',
        'X', 'X', '-']
    player1choice = user_choice(isplayer1_in, board_in, 'X', 'O')

    isplayer1_out = True
    board_out = [
        'X', 'X', 'X',
        'X', 'X', 'X',
        'X', 'X', 'O']
    assert player1choice == (isplayer1_out, board_out)
