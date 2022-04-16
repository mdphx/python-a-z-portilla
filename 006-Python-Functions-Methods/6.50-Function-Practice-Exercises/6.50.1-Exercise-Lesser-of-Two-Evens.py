#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both 
# numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#    lesser_of_two_evens(2,5) --> 5

def lesser_of_two_evens1(num1, num2):
    if num1%2==0 and num2%2==0:
            if num1 < num2:
                result = num1
            else:
                result = num2 
    else:
            if num1 > num2:
                result = num1
            else:
                result = num2
    
    return result

# Another way to write this is with the min() and max() functions.
# The min() function takes two numbers as paramemters and returns the lower of the two
# For example: min(10, 20) will return 10.
#
# The max() function takes two numbers as parameters and returns the higher of the two
# For example: max(10, 20) will return 20.
#
# 
# Here's another way to solve the Lesser of Two Evens problem

def lesser_of_two_evens2(num1, num2):
    if num1%2==0 and num2%2==0:
            result = min(num1, num2)
    else:
            result = max(num1, num2)
    
    return result

# We can also eliminate the result statements by using return statements as follows:

def lesser_of_two_evens3(num1, num2):
    if num1%2==0 and num2%2==0:
           return min(num1, num2)
    else:
           return max(num1, num2)
    
