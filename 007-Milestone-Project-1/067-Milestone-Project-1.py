# Project Scope

#   1. Print a game board.
#   2. Take in player input.
#   3. Place player input on board
#   4. Check game status (ongoing, won, tied, lost)
#   5. Repeat 3 and 4 unitl game is won or tied.
#   6. Ask players if they want to play again

# Function 1:   Write a function that can print out a board.
# Function 2:   Write a function that can take in a player input and assign their marker as 'X' or 'O'
# Function 3:   Write a function that takes in the board list object, a marker ('X' or 'O'), and a 
#               desired position (number 1-9) and assigns it to the board.
# Function 4:   Write a function that takes in a board and checks to see if someone has won.
# Function 5:   Write a function that uses the random module to randomly decide which 
#               player goes first. 
# Function 6:   Write a function that returns a boolean indicating whether a space on the board 
#               is freely available.
# Function 7:   Write a function that checks if the board is full and returns a boolean value. 
#               True if full, False otherwise.
# Function 8:   Write a function that asks for a player's next position (as a number 1-9) 
#               and then uses the function from step 6 to check if its a free position. 
# Function 9:   Write a function that asks the player if they want to play again and returns a 
#               boolean True if they do want to play again.

# Final Step: Use while loops and the functions you've made to run the game!


################################################
# Function 1:   Write a function that can print out a board.
############################################################

#from IPython.display import clear_output

test_board = [ "#", "X", "O", "X", "X", "O", "X", "X", "O", "X"]

def display_board(board):

    # print("")
    print(board[7]+ " | " +board[8]+ " | " +board[9])
    print(board[4]+ " | " +board[5]+ " | " +board[6])
    print(board[1]+ " | " +board[2]+ " | " +board[3])

#Check
#print(display_board(test_board))


# Function 2:   Write a function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():

    #   Output is in the form of a tuple.
    #   OUPUT = (Player 1 marker, Player 2 marker)

    marker = " "

    while marker != "X" and marker != "O":
        marker = input("Player 1: Choose X or O:  ").upper()

    # The following let's us use tuple unpacking to get back the individual markers
    if marker == "X":
        return ("X", "O")
    else:
        return ("0", "X")

#Use tuple unpacking to get the player_markers for each player
player1_marker, player2_marker = player_input()

print(f"Player 1 will be {player1_marker} and Player 2 will be {player2_marker}.")
print("Let the games begin!")

# Function 3:   Write a function that takes in the board list object (a marker "X" or marker "O")
#               and a position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):      
    board[position] = marker

#Test function #3 with test_board ([ "#", "X", "O", "X", "X", "O", "X", "X", "O", "X"])

# place_marker(test_board, "test marker", 8)    # place the marker/choose a marker
# display_board(test_board)                   # display the board showing the marker selection

# Function #4: Write a function that takes in a board list and a marker (X or O) and then checks
#               to see if the marker/move wins the game


def win_check(board, mark):

    #Need to check possible winning combinations
    # A return of True means the player won, a return of False means that player has not won

    #Check all rows and if they share the same marker
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom

    # Check all columns if they share the same marker
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle (left)
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle (center)
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the middle (right)

    # Check two diagonals to see if they share the same marker

    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Check function
print(win_check(test_board, "X"))
print(display_board(test_board))

# Function #5: Write a function that uses the random module to randomly decide which
#               player goes first. Look up random.randint(). Return a string indicating
#               the player that goes first.

import random

def choose_first():
    # We can pass in 0 and 1 and essential have a coin flip.

    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# Function #6:  Write a function that returns a boolean indicating whether a space on the board
#               is open.

def space_check(board, position):
    #open = " " (an empty string)
    return board[position] == " "

# Function #7: Write a function that checks if the board is full and returns a boolean.
#               True if full, False otherwise

def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True

# Function #8: Write a function that asks for a player's next position (number 1-9)
#               and then uses function #6 (space_check(board, position)) to check if it's
#               an open position. If it is, return the position for later use.

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position: (1-9)"))
    
    return position

# Function #9: Write a function that asks the player if they want to play again and returns a boolean
#               True if they want to play again.

def replay():

    choice = input("Play again? Enter Yes or No.")

    return choice == "Yes"



#Step 10 - Use while loops and the above function to run the game!