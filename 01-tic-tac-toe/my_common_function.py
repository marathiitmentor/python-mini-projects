from os import name, system

def greet(what):
    if what == 'start':
        print('********* Welcome to Tic Toc Toe Advanced Version! *********')
    else:
        print('Have a Great Day')

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')