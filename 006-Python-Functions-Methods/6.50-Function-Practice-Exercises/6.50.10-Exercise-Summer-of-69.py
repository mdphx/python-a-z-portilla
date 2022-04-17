#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
 
#   summer_69([1, 3, 5]) --> 9
#   summer_69([4, 5, 6, 7, 8, 9]) --> 9
#   summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(array):
    total = 0
    add=True

    for num in array:
        while add:
            if num != 6:      # while the number is not 6
                total += num  # add the number to the total variable
                break
            else:
                add = False    # if the number is 6 don't do anything
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total