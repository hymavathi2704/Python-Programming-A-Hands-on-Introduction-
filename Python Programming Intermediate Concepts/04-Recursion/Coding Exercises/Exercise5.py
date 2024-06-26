'''
Problem:
Write a recursive function called get_max that takes a list of numbers as a parameter. Return the largest number in the list.
Expected Output:
If the function call is get_max([1, 2, 3, 4, 5]), then the function would return 5
If the function call is get_max([11, 22, 3, 41, 15]), then the function would return 41
'''

#Code:
def get_max(nums):
    # Base case: if the list has only one element, return that element
    if len(nums) == 1:
        return nums[0]
    else:
        # Recursive case: return the maximum of the first element and the maximum of the rest of the list
        return max(nums[0], get_max(nums[1:]))

# Example usage:
print(get_max([1, 2, 3, 4, 5]))     # Output: 5
print(get_max([11, 22, 3, 41, 15])) # Output: 41
