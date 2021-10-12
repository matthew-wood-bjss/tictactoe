from typing import List, Tuple


def user_setup() -> Tuple[str, str]:
    """Function that sets up the game by giving Player 1 the choice of being Token X or O. If an invalid choice is given, try again.
    Args:       None

    Returns:    setup (string): Player 1's token
                setup2 (string): Player 2's token"""
    setup = str(input("Player 1, please choose X or O\n")).upper()
    while setup != "X" and setup != "O":
        setup = str(input("Invalid choice, Player 1, please choose X or O\n")).upper()
    if setup == "X":
        setup2 = "O"
    elif setup == "O":
        setup2 = "X"
    else:
        raise Exception("Choose X or O")
    return setup, setup2


def user_choice(
    isplayer1: bool, board: List[str], p1: str, p2: str
) -> Tuple[bool, List[str]]:
    """Function that gives the respective player's turn the choice of where to go on the board, updates said board and changes whose turn it is.
    If an invalid choice is given, try again.
    Args:       isplayer1 (bool): is it Player 1's turn?
                board (list): current board state containing either "-"s, "X"s or "O"s
                p1 (string): Player 1's token
                p2 (string): Player 2's token

    Returns:    isplayer1 (bool): is it Player 1's turn? (should be opposite to the argument inputted to this function)
                board (list): new board state containing either "-"s, "X"s or "O"s"""
    grid = list(range(10))
    if isplayer1:
        player = 1
    else:
        player = 2
    choice = input(
        "Player {0} choose a spot on the grid\n{1}\n{2}\n{3}\n".format(
            player, grid[0:3], grid[3:6], grid[6:9]
        )
    )
    while (
        choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        or board[int(choice)] != "-"
    ):
        choice = input(
            "Invalid choice, Player {0} choose a spot on the grid\n{1}\n{2}\n{3}\n".format(
                player, grid[0:3], grid[3:6], grid[6:9]
            )
        )
    choice = int(choice)
    if (choice in grid) and (board[choice] == "-") and isplayer1:
        board[choice] = p1
    elif (choice in grid) and (board[choice] == "-") and not isplayer1:
        board[choice] = p2
    else:
        raise Exception("You cannot choose there")
    isplayer1 = not isplayer1
    return isplayer1, board


def is_winner(board: List[str], isplayer1: bool) -> bool:
    """Function that checks if there is any winner with the current board state. If there is, announce the player who just made their turn as
    the winner, if there is a draw also announce there is a draw.
    Args:       isplayer1 (bool): is it Player 1's turn?
                board (list): current board state containing either "-"s, "X"s or "O"s

    Returns:    (bool): Should the game be over?"""
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 4, 8],
        [2, 4, 6],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
    ]
    for i in wins:
        if all(["X" == board[j] for j in i]) or all(["O" == board[j] for j in i]):
            if isplayer1:
                print("Congratulations Player 2!")
            else:
                print("Congratulations Player 1!")
            return True
    if "-" not in board:
        print("Draw")
        return True
    else:
        return False


def print_board(board: List[str]) -> None:
    """Function to print the current board state.
    Args:       board (list)

    Returns:    None"""
    print(
        "Current board state:\n{0}\n{1}\n{2}\n".format(
            board[0:3], board[3:6], board[6:9]
        )
    )


def main():
    """Function to start the game. continues to play and only ends if someone has won the game or there is a draw.
    Args:       None

    Returns:    None"""
    isplayer1 = True
    board = ["-" for i in range(9)]
    print_board(board)
    won = False
    p1, p2 = user_setup()
    while won is False:
        isplayer1, board = user_choice(isplayer1, board, p1, p2)
        print_board(board)
        won = is_winner(board, isplayer1)


if __name__ == "__main__":
    main()
