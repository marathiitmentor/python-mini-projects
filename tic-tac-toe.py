from os import name, system

# On start of game it will pass start & it will greet as welcome and at end it will print Good Day 
def greet(what):
    if what == 'start':
        print('Welcome to Tic Toc Toe!')
    else:
        print('Nice Played! Have a Great Day')

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_board(board):
    i = 0
    while i<8:
        print(f'{board[i]}  |  {board[i+1]}  |  {board[i+2]}')
        print('--------------')
        i+=3

def player_input():
    player1 = input("Please pick a marker 'X' or 'O'")

# The game begins... 9th June 26
clear_screen()
greet('start')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
player_input()

greet('stop')
