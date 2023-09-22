import os
game_board = [['-', '-', '-'],
              ['-', '-', '-'],
              ['-', '-', '-']]

tic_tac_toe = """
  _______          ______               ______         
 /_  __(_)____    /_  __/___ ______    /_  __/___  ___ 
  / / / / ___/_____/ / / __ `/ ___/_____/ / / __ \/ _ \\
 / / / / /__/_____/ / / /_/ / /__/_____/ / / /_/ /  __/
/_/ /_/\___/     /_/  \__,_/\___/     /_/  \____/\___/ 
                                                       
"""


def clear_board_game(game_board):
    """clear the board game every new game
    Args:
        game_board: A 3x3 list of strings representing the game board.

    Returns:
        None.    
    """
    for row in game_board:
        for (index,column) in enumerate(row):
            row[index] = "-"



def print_game_board(game_board):
    """Prints the game board to the console.

    Args:
        game_board: A 3x3 list of strings representing the game board.

    Returns:
        None.
    """
    for row in game_board:
        print(' '.join(row))


def handle_player_move(game_board, player_symbol):
    """Prompts the user for a move and updates the game board.

    Args:
        game_board: A 3x3 list of strings representing the game board.
        player_symbol: The player's symbol ('X' or 'O').

    Returns:
        None.
    """
    row = int(input('Enter row: '))
    column = int(input('Enter column: '))

    if row < 0 or row > 2 or column < 0 or column > 2:
        print('Invalid move. Please enter a valid row and column.')
        handle_player_move(game_board, player_symbol)
        return

    # Update the game board
    if (game_board[row][column]) == '-':
        game_board[row][column] = player_symbol
    else:
        print("Try different move...")
        handle_player_move(game_board, player_symbol)


def check_for_win(game_board, player_symbol):
    """Checks if the player has won the game.

    Args:
        game_board: A 3x3 list of strings representing the game board.
        player_symbol: The player's symbol ('X' or 'O').

    Returns:
        True if the player has won the game, False otherwise.
    """
    # Check rows
    for row in game_board:
        if row[0] == row[1] == row[2] == player_symbol:
            return True

    # Check columns
    for column in range(3):
        if game_board[0][column] == game_board[1][column] == game_board[2][column] == player_symbol:
            return True

    # Check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player_symbol or \
            game_board[0][2] == game_board[1][1] == game_board[2][0] == player_symbol:
        return True

    return False


def check_for_tie(game_board):
    """Checks if the game is tied.

    Args:
        game_board: A 3x3 list of strings representing the game board.

    Returns:
        True if the game is tied, False otherwise.
    """
    for row in game_board:
        for square in row:
            if square == '-':
                return False

    return True


def start_game():
    clear_board_game(game_board)
    current_player = 'X'

    while True:
        # Print the game board

        # Prompt the current player for their move
        handle_player_move(game_board, current_player)
        print_game_board(game_board)
        # Check if the current player has won
        if check_for_win(game_board, current_player):
            print(current_player + ' wins!')
            break

        # Check if the game is tied
        if check_for_tie(game_board):
            print('Tie game!')
            break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


def main():
    play_again = 1
    while play_again:
        # Clearing the Screen
        os.system('cls')
        print(tic_tac_toe)
        start_game()
        print("Do you wanna play again? (y/n)")
        if input() == "y":
            play_again = 1
        else:
            play_again = 0


if __name__ == '__main__':
    main()
