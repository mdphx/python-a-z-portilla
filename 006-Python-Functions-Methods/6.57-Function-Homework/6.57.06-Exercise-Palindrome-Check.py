#Write a function that check if a word or phrase is a palindrome.

#The return value should be a boolean.

#Example input: "nurses run"
#Expected output: True

def palindrome(string):

    #Remove any spaces from a string
    string=string.replace(" ", "")

    #Check if string is == the reverse version of the string
    return string == string[::-1] 

print(palindrome("nurses run"))