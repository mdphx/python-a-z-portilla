#Write a python function that takes a list and returns a new list with unique elements of the first list.

#Sample list: [1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
#Unique list: [1, 2, 3, 4, 5]

#Solution #1 - convert to a set then cast to a list
def unique_list1(original_list1):
    #first do a set(original_list) to return a set {1, 2, 3, 4, 5}
    #then wrap the set it in the list() function to cast it to a list
    return list(set(original_list1))

print(unique_list1([1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


#Solution #2 - 
def unique_list2(original_list2):
    #create placeholder list and append items to the placeholder
    unique_numbers = []

    for number in original_list2:
        if number not in unique_numbers:    #if the number isn't already in the unique_numbers list
            unique_numbers.append(number)   #add the number to the list
    return unique_numbers                   #when the loop is complete return the unique_numbers list

print(unique_list2([1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))