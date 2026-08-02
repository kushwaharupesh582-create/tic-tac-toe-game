def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 to 9 (left to right, top to bottom):")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    while True:
        board = [" "] * 9
        current_player = "X"
        game_over = False

        while not game_over:
            print_board(board)
            print(f"Player {current_player}'s turn.")

            try:
                position = input("Enter a position (1-9) or 'q' to quit: ")

                if position.lower() == 'q':
                    print("Thanks for playing! Goodbye.")
                    return

                pos = int(position) - 1

                if pos < 0 or pos > 8:
                    print("Position must be between 1 and 9. Try again.")
                    continue

                if board[pos] != " ":
                    print("That spot is already taken! Choose another.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a number (1-9) or 'q'.")
                continue

            board[pos] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins! 🎉")
                game_over = True
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie! 🤝")
                game_over = True
                break

            current_player = "O" if current_player == "X" else "X"

        while True:
            again = input("Do you want to play again? (y/n): ").lower()
            if again == 'y':
                break
            elif again == 'n':
                print("Thanks for playing! Goodbye.")
                return
            else:
                print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play_tic_tac_toe()