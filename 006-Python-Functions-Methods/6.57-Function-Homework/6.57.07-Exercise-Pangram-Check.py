#Write a function to check if a string is a pangram.
#Assume the string has no punctuation

#Sample input: "The quick brown fox jumps over the lazy dog"
#Expected output: True

#Note: Pangrams are words or sentences that contain ever letter in the alphabet at least once.

#Hints: 
# - Consider using the .replace() method to remove spaces
# - Look at the string module
# - Look at set comparisons

import string

def ispangram1(str1, alphabet=string.ascii_lowercase):
    #Create a set of the entire alphabet
    alphaset = set(alphabet)
    

    #Remove spaces from input string
    str1 = str1.replace(" ", "")


    #Convert string to lowercase
    str1 = str1.lower()


    #Grab all unique letters from the string set()
    str1 = set(str1)

    #Compare alphabet set to string set.
    return str1 == alphaset

print(ispangram1("The quick brown fox jumps over the lazy dog", alphabet=string.ascii_lowercase))
print(ispangram1("Sally sells seashells by the sea shore", alphabet=string.ascii_lowercase))


