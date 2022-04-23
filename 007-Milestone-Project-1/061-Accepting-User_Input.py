#Input function review

#This will return the statement "Please enter a value______"
#But as-is, any value entered will not be return.

#input("Please enter a value _________")

#To store the input value, we can assign the input value to a variable, for example
#a variable called result:

#result1 = input("Please enter a value _________")
#print(result1)

#the input() function always returns a string. To change the datatype to integer as 
# follows

result2 = input("Please enter a value _________")
#print(result2)
#print(type(result2)) #print datatype
result2_int = int(result2) #convert string to integer
print(result2_int)
print(type(result2_int)) # print datatype after change

#Use the type() function if you need a specific data type in your function

#Going back to the tic-tac-toe game...

ex_row1 = [ ' ', ' ', ' ']
ex_row2 = [ ' ', ' ', ' ']
ex_row3 = [ ' ', ' ', ' ']

#If we want someone to choose an index position
position_index1=input("Choose an index position: ")

#if we want to pass in the position_index variable to one of ex_row lists, we must convert position_index to
# an integer, because list indexes must be integers or slices. Ex. ex_row1[2]

#we can convert the position_index result to an integer using the int() function or
#wrap the input () function in the int() function as follows
ex_row4=[8, 9, 10, 11, 12, 13, 14]
position_index2=int(input("Choose an index position: "))

#then we can access indexes in the lists using the position_index variable:

print(ex_row4[position_index2])
