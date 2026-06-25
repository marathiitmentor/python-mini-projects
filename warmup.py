from os import name, system

def display_game(game_list):
    print('Here is the current list')
    print(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        choice = input('Pick a position to replace (0,1,2): ')

    if choice not in ['0','1','2']:
        clear_output()
        print("Sorry, but you did not choose a valid position (0,1,2)")

    clear_output()    
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at the position: ")

    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = input('Enter Y to continue, N to stop: ')   

    while choice not in ['Y','N']:
        clear_output()
        choice = input('Sorry, I didn\'t understand. Please make sure to choose Y or N.: ')

    if choice == 'Y':
        return True
    else:
        return False    

def clear_output():
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 


# Here the game sarts...
# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2]

while game_on:
    
    # Clear any historical output and show the game list
    clear_output()
    display_game(game_list)
    
    # Have player choose position
    position = position_choice()
    
    # Rewrite that position and update game_list
    game_list = replacement_choice(game_list,position)
    
    # Clear Screen and show the updated game list
    clear_output()
    display_game(game_list)
    
    # Ask if you want to keep playing
    game_on = gameon_choice()