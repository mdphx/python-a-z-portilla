#Write a function that accepts a string and calculates the number of uppercase and lowercase letters.
#For example: "Hello Mr. Rogers, how are you this fine Tuesdsay?"

#Expected output:
#No of uppercase characters: 4
#No of lowercase characters: 33

#Hint: Consider using string methods .isupper() and .islower()
#If ambitious explore the Collections module to solve this problem

#Solution #1
def up_low1(string):
    #Counter to keep track of characters
    uppercase = 0
    lowercase = 0

    #for loop to iterate string
    for char in string:      #for each character in the string
        if char.isupper():   #if the character is uppercase
            uppercase += 1   #add the character to the uppercase counter
        elif char.islower(): #if the character is lowercase
            lowercase += 1   #add the character to the lowercase counter
        else:                #else
            pass             #skip the character and do nothing. Ex. punctuation
    #After the loop is complete, print the following:
    print(f"Original String: {string}")
    print(f"Uppercase count: {uppercase}")
    print(f"Lowercase count: {lowercase}")
    

up_low1("Hello Mr. Rogers, how are you this fine Tuesdsay?")

#Solution 2 - Using a Dictionary
def up_low2(string):
    #Counter to keep track of characters
    my_dictionary = {"upper": 0, "lower":0}

    #for loop to iterate string
    for char in string:                     #for each character in the string
        if char.isupper():                  #if the character is uppercase
            my_dictionary["upper"] += 1     #add the character to the uppercase counter
        elif char.islower():                #if the character is lowercase
            my_dictionary["lower"] += 1     #add the character to the lowercase counter
        else:                               #else
            pass                            #skip the character and do nothing. Ex. punctuation
    #After the loop is complete, print the following:
    print(f"Original String: {string}")
    print(f"Uppercase count: {my_dictionary['upper']}")
    print(f"Lowercase count: {my_dictionary['lower']}")
    

up_low2("Hello Mr. Rogers, how are you this fine Tuesdsay?")