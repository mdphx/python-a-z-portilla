
#You could have three different print functions like the following
print([1, 2, 3])
print([4, 5, 6])
print([7, 8, 9])

#Instead of calling print three time, I can create a function so I only have to
# do one function call. 

def display (row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

ex_row = [1, 2, 3]

display(ex_row, ex_row, ex_row)

# It's also more flexible, because I can pass in different lists 
# Thinking about the tic-tac-toe game, we can create three lists of empty strings then call the funciton

ex_row1 = [ ' ', ' ', ' ']
ex_row2 = [ ' ', ' ', ' ']
ex_row3 = [ ' ', ' ', ' ']

display(ex_row1, ex_row2, ex_row3)

#each empty item in the list can map to a position on the tic-tac-toe board
#for example, row2[1] maps to the center position on the board.

ex_row2[1] = "X"

display(ex_row1, ex_row2, ex_row3) 

# the output is as follows:
# [' ', ' ', ' ']
# [' ', 'X', ' ']
# [' ', ' ', ' ']