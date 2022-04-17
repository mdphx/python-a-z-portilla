#### OLD MACDONALD: Write a function that capitalizes the first and fourth 
# letters of a name
     
#   old_macdonald('macdonald') --> MacDonald
    
#  Note: `'macdonald'.capitalize()` returns `'Macdonald'`

#Using the Upper method

def old_macdonald1(name):

    first_letter = name[0] #grab first letter
    inbetween = name [1:3] #grab characters from index 1 up to but not including index 3
    fourth_letter = name[3] #grab the letter at index 3
    rest = name[4:] #grab the letters starting at index 4 until the end of the string

    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

old_macdonald1("macdonald") #invoke the function

#Using the Capitalize method

def old_macdonald2(name):
    first_part= name[:3] #grab the letters from the beginning up to but not including index 3
    second_part = name[3:] #grab the letters from index 3 to the end of the string

    return first_part.capitalize() + second_part.capitalize()

old_macdonald2("macdonald") #invoke the function



