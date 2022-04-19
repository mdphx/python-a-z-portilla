#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 
# in order. (Doesn't mean consecutive order)

#     spy_game([1,2,4,0,0,7,5]) --> True
#     spy_game([1,0,2,4,0,5,7]) --> True
#     spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):

    code = [0, 0, 7, "x"]   #we will compare the sequence of numbers in this code list to the list of numbers
                            #passed in as an argument.

    #After first iteration - [0, 7, "x"] - after the first iteration the first 0 is popped off the code list.
    #After second iteration - [7, "x"] - second 0 is popped off the code list.
    #After third iteration - ["x"] - only one parameter is left. And the value of the list is 1
    
    for num in nums:
        if num == code[0]:
            code.pop(0) #the pop() method removes the item at the specified index.
    return len(code) == 1 #Returns true with the length of the list is equal to one.