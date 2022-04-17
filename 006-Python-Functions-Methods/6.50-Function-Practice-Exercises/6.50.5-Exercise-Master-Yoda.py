#### MASTER YODA: Given a sentence, return a sentence with the words reversed

 #   master_yoda('I am home') --> 'home am I'
 #    master_yoda('We are ready') --> 'ready are We'
    
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

#    >>> "--".join(['a','b','c'])
#    >>> 'a--b--c'
# 
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
# 
#     >>> " ".join(['Hello','world'])
#     >>> "Hello world"


#Example 1 - splitting a into a list, and reversing the list.
def master_yoda1(text):

    # First step is to get a list of the words.
    wordlist = text.split() 

    #Reverse the wordlist
    reverse_wordlist = wordlist[::-1]

    return reverse_wordlist #returns the wordlist in reverse order.

 master_yoda1("I am home")   

# Example 2
# Now we need to join the list together
def master_yoda2(text):

    # First step is to get a list of the words.
    wordlist = text.split() 

    #Reverse the wordlist
    reverse_wordlist = wordlist[::-1]

    return ' '.join(reverse_wordlist) #returns the wordlist as a string in reverse order.




#note on What's happening in wordlist[::-1]:   
# - By leaving the start argument empty, we're saying start at the beginning of the string.
# - By leaving the stop argument empty, we're saying go all the way to the end of the string.
# - By specifying -1 as the step argument, we're saying start from the end of the string and return each character.

