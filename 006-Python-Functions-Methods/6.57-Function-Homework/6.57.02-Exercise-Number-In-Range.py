#Write a function that check if a number is in a given range
#inclusive of high and low

#To return a boolean
def run_check1(num, low, high):
    return num in range(low, high+1)

print(run_check1(5, 2, 7))
print(run_check1(11, 2, 7))

#To return a string
def run_check2(num, low, high):
    if num in range(low, high+1):
        print(f"The number {num} is in the range of {low} and {high}.")
    else:
        print(f"The number {num} is not in range of {low} and {high}.")

run_check2(5, 2, 7) #don't need to run this is the print function since we say to print the result in the function.
run_check2(11, 2, 7)