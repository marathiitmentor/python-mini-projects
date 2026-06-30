from os import name, system


# On start of game it will pass start & it will greet as welcome and at end it will print Good Day 
def greet(what):
    if what == 'start':
        print('Welcome to Tic Toc Toe!')
    else:
        print('Have a Great Day')

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_board(board):
    clear_screen()
    # i = 0
    # while i<8:
    #     print(f'{board[i]}  |  {board[i+1]}  |  {board[i+2]}')
    #     print('--------------')
    #     i+=3
  
    print(f'{board[6]}  |  {board[7]}  |  {board[8]}')
    print('---+-----+---')
    print(f'{board[3]}  |  {board[4]}  |  {board[5]}')
    print('---+-----+---')
    print(f'{board[0]}  |  {board[1]}  |  {board[2]}')

def player_input():
    marker = input("Please pick a marker 'X' or 'O'>  ")
    return marker

def place_marker(board, marker, position):
    # Need validation logic here before adding into board
    board[position-1] = marker.upper()
    does_win = win_check(board, marker.upper())
    return does_win

def win_check(board, marker):
    if (
            board[0] == board[1] == board[2] == marker or
            board[3] == board[4] == board[5] == marker or
            board[6] == board[7] == board[8] == marker or
            board[0] == board[3] == board[6] == marker or
            board[1] == board[4] == board[7] == marker or
            board[2] == board[5] == board[8] == marker or
            board[0] == board[4] == board[8] == marker or
            board[2] == board[4] == board[6] == marker
    ):
        return True
    return False

def replay():
    choice = input("Do you want to play further? ")
    if choice=='Y' or choice=='y':
        return True
    
    return False

def player_choice(board):
    position = input(f'Enter your position (1-9): ')
    # Add logic to check board for given position. Right now just sending back the position    
    curpos = int(position)
    if board[curpos-1] != ' ':
        return -1
    
    return curpos

def full_board_check(board):
    for val in board:
        if val == ' ':
            return False
    return True


# The game begins... 9th June 26
clear_screen()
greet('start')
game_board = [' ' for _ in range(0,9)]
display_board(game_board)

choice = True
while choice == True:   
    marker = player_input()
    position = player_choice(game_board)
    if position == -1:
        temp = input('Sorry! Place is filled already. Enter Y to continue: ')
        if temp == 'Y' or temp == 'y':
            choice = True
        else:
            choice = False
    else:    
        is_full = full_board_check(game_board)
        if is_full == True:
            choice=False
            print('Sorry! Board is full. Thank you for playing.')
            break
        
        does_win = place_marker(game_board, marker, position)
        display_board(game_board)
    
        if does_win == True:
            choice=False
            print(f'{marker} Won!')
        else:
            choice = replay()

greet('stop')