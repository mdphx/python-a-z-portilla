#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
#   paper_doll('Hello') --> 'HHHeeellllllooo'
#    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    result = " " #start with an empty string

    for char in text:           # loop through each character in the string.
            result += char*3    # multiply each character by three.
    return result               # return the result.

output=paper_doll("Hello")
print(output)
