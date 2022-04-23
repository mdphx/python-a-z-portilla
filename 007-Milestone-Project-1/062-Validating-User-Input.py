#use a while loop to validate user input

def user_choice():

    choice="wrong" #assign false value
    acceptable_range = range(0, 11)
    within_range=False

    
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10):   ")

        #VALIDATE DATATYPE
        if choice.isdigit() == False:
            print("Sorry that is not a digit. Please try again.")
    
        #VALIDATE RANGE (between 0 and 10)
        #check against a list of acceptable values
        #create a list, use in or not in to check if value is in list.
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Number must be between 0 and 10")
                within_range = False

    return int(choice)

print(user_choice())