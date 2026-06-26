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
    i = 0
    while i<8:
        print(f'{board[i]}  |  {board[i+1]}  |  {board[i+2]}')
        print('--------------')
        i+=3

def player_input():
    player1 = input("Please pick a marker 'X' or 'O':  ")
    return player1

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

# The game begins... 9th June 26
clear_screen()
greet('start')
test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

choice = True

while choice == True:    
    ch = player_input()
    win_check(test_board,ch)
    choice = replay()

greet('stop')
