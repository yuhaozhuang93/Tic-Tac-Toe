board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} | <= | 1 | 2 | 3 |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} | <= | 4 | 5 | 6 |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} | <= | 7 | 8 | 9 |".format(board[6],board[7],board[8])

    print("                   Location number")
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == "x":
        number = 1
    elif icon == "o":
        number = 2
        
    print("Your turn player{}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice-1] == "  ":
        board[choice-1] = icon
    else:
        print()
        print("That blank is taken!")

def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if "  " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("x")
    print_board()
    if is_victory("x"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("Its draw!")
        break
    player_move("o")
    if is_victory("o"):
        print_board()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("Its draw!")
        break

    



