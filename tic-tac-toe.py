from os import name, system

marker1 = None
marker2 = None
turn = None

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
    i = 0
    while i<8:
        print(f'{board[i]}  |  {board[i+1]}  |  {board[i+2]}')
        print('--------------')
        i+=3

def player_input():
    ch = input("Please pick a marker 'X' or 'O':  ")
    if ch == 'X':
        marker1 = 'X'
        marker2 = 'O'
    elif ch == 'O':
        marker1 = 'O'
        marker2 = 'X'
    else:
        marker1 = 'X'
        marker2 = 'O'
    print(f'Player 1 have {marker1} & Player 2 have {marker2}')
    turn = 'player1' # add logic here to choose player randomly.

def place_marker(board, marker, position):
    board[position-1] = marker

def win_check(board, mark):
    display_board(board)

def replay():
    choice = input("Do you want to play further? ")
    if choice=='Y' or choice=='Yes':
        print("Nice! Keep Playing")
        return True
    else:
        print("Well Played!")
        return False

def player_choice(board):
    position = input(f'Enter your position (1-9): ')
    if turn == 'player1':
        place_marker(board, marker1, position)
        turn = 'player2'
    else:
        place_marker(board, marker2, position)
        turn = 'player1'


# The game begins... 9th June 26
clear_screen()
greet('start')
game_board = [' ' for _ in range(0,9)]
display_board(game_board)

player_input()

choice = True
while choice == True:   
    player_choice(game_board)
    display_board(game_board)
    # win_check(game_board,ch)
    choice = replay()

greet('stop')

https://chatgpt.com/share/6a3de5ea-88c8-83e8-a664-44a1c1a87bea