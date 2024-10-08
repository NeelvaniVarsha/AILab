import random

board = [' ' for _ in range(9)]

def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def has_won(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def bot_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if has_won('O'):
                return
            board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if has_won('X'):
                board[i] = 'O'
                return
            board[i] = ' '

    possible_moves = [i for i, x in enumerate(board) if x == ' ']
    if possible_moves:
        move = random.choice(possible_moves)
        board[move] = 'O'
    else:
        print("It's a draw!")
        exit()


def main():
    current_player = 'X'
    while True:
        print_board()
        if current_player == 'X':
            move = input("Player X, enter your move (1-9): ")
            if board[int(move) - 1] != ' ':
                print("Invalid move, try again.")
                continue
            board[int(move) - 1] = current_player
        else:
            bot_move()
            print("Bot O has made its move.")
        if has_won(current_player):
            print_board()
            if current_player == 'X':
                print("Player X wins! Congratulations!")
            else:
                print("Bot O wins! Better luck next time!")
            break
        if ' ' not in board:
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
