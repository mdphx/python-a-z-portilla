#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
#    count_primes(100) --> 25

#By convention, 0 and 1 are not prime.

#Solution #1

def count_primes1(num):
    #Check for 0 or 1 input
    if num < 2:
        return 0

    ##################
    # Check for 2 or greater
    #################

    #Store prime numbers in this list
    primes =[2]

    #Counter going up to the input num

    x = 3 #this is a counter

    # x is going through every number to the input number
    while x <= num:
        for y in range(3,x,2): #step size of two because they will all be even/non-prime numbers
            if x%y == 0: #if the number is ever divisible by x
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

output1 = count_primes1(100)
print(output1)

## Another way to invoke and print the function output

print(count_primes1(50))
