#Write a function to multiply all the numbers in a list
#Sample list: [1, 2, 3, -4]
#Expected output: -24


def multiply(numbers):

    #for multiplication we initialize the counter to 1.
    #if we intialize it to 0, when the for loop ran we would be multiplying the pass in numbers by 0
    #and any number multiplied by 0 is zero.
    total = 1                   
    for num in numbers:
        total = total * num     #take the total and multiply by a number. Set the Total variable to the new product.
    return total

print(multiply([1, 2, 3, -4]))
