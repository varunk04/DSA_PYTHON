"""
 Problem - Rotated Lists:
------------------------------------------

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. 
You can assume that all the numbers in the list are unique.
Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element.
E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`.

"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.

"""
"""
Possible Test Cases:
-------------------------------

Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible 
variations we might encounter: 

1. A list of size 10 rotated 3 times.
2. A list of size 8 rotated 5 times.
3. A list that wasn't rotated at all.
4. A list that was rotated just once. 
5. A list that was rotated `n-1` times, where `n` is the size of the list.
6. A list that was rotated `n` times (do you get back the original list here?)
7. An empty list.
8. A list containing just one element.

We'll express our test cases as dictionaries, to test them easily. Each dictionary will contain 2 keys: `input` (a 
dictionary itself containing one key for each argument to the function and `output` (the expected result from the 
function). Here's an example. 
"""
tests = [
    {  # list size of 10 rotated 3 times
        'inputs': {
            'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
        },
        'output': 3
    },
    {  # list size of 8 rotated 5 times
        'inputs': {
            'nums': [4, 5, 6, 7, 8, 1, 2, 3]
        },
        'output': 5
    },
    {  # list size of 3 rotated 1 time
        'inputs': {
            'nums': [7, 3, 5]
        },
        'output': 1
    },
    {  # list size of 6 rotated 6 times
        'inputs': {
            'nums': [3, 5, 7, 8, 9, 10]
        },
        'output': 0
    }
]

'''
If we check the rotated list we can see that the position of the smallest element in the list is the number of 
times the list was rotated, so the problem is all about finding the position of the smallest element which is a 
searching operation. 
'''


def count_rotations_linear(nums):
    position = 0  # start wih zero position that is first element

    while position < len(nums):
        # Criteria: number at the current position is less than the predecessor.
        if position > 0 and nums[position] < nums[position - 1]:
            return position

        # Move to next position
        position += 1

    return 0


def count_rotations_binary(nums):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        mid_number = nums[mid]

        print('lo:', lo, "hi:", hi, 'mid:', mid, 'mid_number:', mid_number)

        if mid > 0 and (nums[mid - 1] >= mid_number and mid_number <= nums[mid + 1]):
            return mid
        elif mid_number <= nums[hi]:
            hi = mid - 1
        else:
            lo = mid + 1

    return 0


for test in tests:
    result = count_rotations_binary(**test['inputs'])
    print('input :', test['inputs'])
    print('expected output:', test['output'])
    print('function output:', result)
    print(result == test['output'])
