'''
Andy Walsh
Tic Tac Toe
Sep. 23
'''



print("Welcome to my dope game, lets play Tic-Tac-Toe!")

import random

# this is the board 2d-array
board = [["_","_","_"],["_","_","_"],["_","_","_"]]
win_x = [["X","X","X"],["X","X","X"],["X","X","X"]]
win_O = [["O","O","O"],["O","O","O"],["O","O","O"]]

def print_board():
    print("columns 0    1    2")
    print("Row-0",board[0])
    print("Row-1",board[1])
    print("Row-2",board[2])

# do error handling here
# this code sets values
def player_choosing():
    player_choice = input ("Would you like to be X or O?")
    print("Great you are", player_choice )
    if (player_choice != "X") and (player_choice != "O"):
        print("Learn your letters dummy.")
        player_choosing()
    if player_choice == "X":
        computer_choice = "O"
        print("The computer is", computer_choice)
    if player_choice == "O" :
        computer_choice = "X"
        print("The computer is", computer_choice)
player_choosing()

def computer_move():
    ran_choice_row = random.randint(0,2)
    ran_choice_column = random.randint(0, 2)

    if board[ran_choice_row][ran_choice_column] == "_":
        board[ran_choice_row][ran_choice_column] = computer_choice
        print_board()
    else:
        computer_move()

def user_move():
    user_choice_row = input("What row would you like?")
    user_choice_column = input("What column would you like?")
    int_user_choice_row = int(user_choice_row)
    int_user_choice_column = int(user_choice_column)
    if board[int_user_choice_row][int_user_choice_column] == "_":
        board[int_user_choice_row][int_user_choice_column] = player_choice
        print_board()
    else:
        print("Pick again.")
        user_move()

def win_conditions():
    while True:
        if win_x[0] == board[0]:
            print("Player X wins!")
            break
        if win_x[1] == board[1]:
            print("Player X wins!")
            break
        if win_x[2] == board[2]:
            print("Player X wins!")
            break
        if win_O[0] == board[0]:
            print("Player O wins!")
            break
        if win_O[1] == board[1]:
            print("Player O wins!")
            break
        if win_O[2] == board[2]:
            print("Player O wins!")
            break
        if (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0]) == "X":
            print("Player X wins!")
            break
        if (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1]) == "X":
            print("Player X wins!")
            break
        if (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2]) == "X":
            print("Player X wins!")
            break
        if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0]) == "O":
            print("Player O wins!")
            break
        if (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1]) == "O":
            print("Player O wins!")
            break
        if (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2]) == "O":
            print("Player O wins!")
            break
        user_move()
        if win_x[0] == board[0]:
            print("Player X wins!")
            break
        if win_x[1] == board[1]:
            print("Player X wins!")
            break
        if win_x[2] == board[2]:
            print("Player X wins!")
            break
        if win_O[0] == board[0]:
            print("Player O wins!")
            break
        if win_O[1] == board[1]:
            print("Player O wins!")
            break
        if win_O[2] == board[2]:
            print("Player O wins!")
            break
        if (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0]) == "X":
            print("Player X wins!")
            break
        if (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1]) == "X":
            print("Player X wins!")
            break
        if (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2]) == "X":
            print("Player X wins!")
            break
        if (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0]) == "O":
            print("Player O wins!")
            break
        if (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2]) == "O":
            print("Player O wins!")
            break
        if (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2]) == "O":
            print("Player O wins!")
            break
        if (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2]) == "X":
            print("Player X wins!")
            break
        if (board[0][1] == "X") and (board[1][1] == "X") and (board[2][0]) == "X":
            print("Player X wins!")
            break
        if (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2]) == "O":
            print("Player O wins!")
            break
        if (board[0][1] == "O") and (board[1][1] == "O") and (board[2][0]) == "O":
            print("Player O wins!")
            break

def gameplay():
    while True:
        computer_move()
        win_conditions()
        user_move()
        win_conditions()

gameplay()

