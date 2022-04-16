#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#    animal_crackers('Levelheaded Llama') --> True
#    animal_crackers('Crazy Kangaroo') --> False

def animal_crackers1(text):
    wordlist =  text.split
    print(wordlist) # to verify list

    first = wordlist[0] #the first word is equal to the word in the list at index 0
    second= wordlist[1] #the second word is equal to the word in the list at index 2

    return first[0] == second[0]    #first[0] is equal to the first letter in the first word
                                    #second[0] is equal to the first letter in the second word

# Another way to write this is

def animal_crackers2(text):
    wordlist =  text.split
    print(wordlist) #to verify list

    first = wordlist[0] #the first word is equal to the word in the list at index 0
    second= wordlist[1] #the second word is equal to the word in the list at index 2

    return wordlist[0][0] == wordlist[1][0]    #Returns True if equal, else False.
                                                #This is called a double index call
    
    # wordlist[0][0]
    #   The first index is equal to the the first item in the word list.
    #   the second index is equal to the first letter 
    # 
    # wordlist[1][0] 
    #   The first index is equal to the second item in the word list
    #   The second index is equal to the first letter in that item

    # To match case of the letters, we can do this:

def animal_crackers3(text):
    wordlist =  text.lower().split() #convert all items in the wordlist to lowercase before doing the split
    print(wordlist)

    first = wordlist[0] 
    second= wordlist[1] 

    return wordlist[0][0] == wordlist[1][0]    #Returns True if equal, else False.
                                               
                                   