from tictactoetest import __version__
from tictactoetest.tictactoe import is_winner

def test_version():
    assert __version__ == '0.1.0'

def test_is_winner():
    assert is_winner([\
        '-','-','-',\
        '-','-','-',\
        '-','-','-'],True) == False

def test_is_winner2():
    assert is_winner([\
        'X','-','O',\
        '-','X','O',\
        '-','-','X'],True) == True

def test_is_winner3():
    assert is_winner([\
        'X','O','O',\
        'O','X','X',\
        'X','O','O'],True) == True

def test_is_winner4():
    assert is_winner([\
        'O','X','O',\
        '-','O','O',\
        '-','X','X'],False) == False