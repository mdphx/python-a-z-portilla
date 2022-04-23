#Create a simple interactive program
#The program will:
#   - Display a list
#   - Accept and validate user input. 
#   - Update the list with the user input.

# Need the following functions:
#   Function #1: Display game.
#   Function #2: Player chooses (index) position.
#   Function #3: Player enters new value for (index) position.
#   Function #4: Option to continue or quit game.

###########################################################################
#     Function #1: Display Game
###########################################################################

game_list = [0, 1, 2] #default/starting game list

def display_game(game_list):
    print("Here is the current list:  ")
    print(game_list)

#check
#print(display_game(game_list))

###########################################################################
#     Function #2: Player chooses (index) position
###########################################################################

def position_choice():
    choice ="wrong"

    while choice not in ["0", "1", "2"]:
        choice = input("Pick a position (0, 1, 2):  ")
        if choice not in ["0", "1", "2"]:
            print("Not a valid choice. Please try again.")

    return int(choice)
#check
#print(position_choice())

###########################################################################
#     Function #3: Player enters new value for (index) position
###########################################################################

def replacement_choice(game_list, position):

    user_placement = input("Type of string to place at position:  ")

    game_list[position] = user_placement

    return game_list

#check
#print(replacement_choice(game_list, 2))

###########################################################################
#     Function #4: Option to continue or quit game
###########################################################################

def gameon_choice():
    choice ="wrong"

    while choice not in ["Y", "N"]:
        choice = input("Keep playing? (Y or N):  ")
        if choice not in ["Y", "N"]:
            print("Please enter Y or N")

    if choice == "Y":
        return True
    else:
        return False

#check
#print(gameon_choice())

###########################################################################
#     Putting it all together
###########################################################################

def run_game():
    game_on = True
    game_list = [0, 1, 2]

    while game_on:
    
        display_game(game_list)

        position = position_choice()

        game_list = replacement_choice(game_list, position)

        display_game(game_list)

        game_on = gameon_choice()

print(run_game())