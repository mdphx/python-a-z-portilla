# Coding Exercise #9 - Pick Evens

# Define a function called myfunc that takes in an arbitrary number of arguments and
# returns a list containing only those arguments that are even.

def myfunc(*args):
    mylist = []
   
    for num in args:
        if num%2 == 0:
            mylist.append(num)
    return mylist