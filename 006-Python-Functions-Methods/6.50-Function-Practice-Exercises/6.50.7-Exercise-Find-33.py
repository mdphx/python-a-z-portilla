#### FIND 33: 

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#     has_33([1, 3, 3]) → True
#     has_33([1, 3, 1, 3]) → False
#     has_33([3, 1, 3]) → False

def has_33(nums):
    for index in range(0, len(nums)-1):
        if nums[index] == 3 and nums [index+1] ==3:
            return True
    return False

result1 = has_33([1, 3, 3]) #invoke function. Should return True.
print(result1)

result2 = has_33([3, 1, 3]) #invoke function. Should return False.
print(result2)