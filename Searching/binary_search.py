"""
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""
import time


def test_location(cards, query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card_binary(cards, query):
    # Create a variables to hold first and last position of the cards elements:
    lo, hi = 0, len(cards) - 1

    # set up a loop for repetition:
    while lo <= hi:

        # Calculating the mid of the cards list:
        mid = (hi + lo) // 2
        result = test_location(cards, query, mid)

        # check if element at the current position matches the query
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    return -1


# Test cases to validate against:
tests = [
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    },
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    },
    {
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    },
    {
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    },
    {
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    },
    {
        'input': {
            'cards': [],
            'query': -127
        },
        'output': -1
    },
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    }
]

for test in tests:
    start = time.time()
    result = locate_card_binary(**test['input'])
    print('input :', test['input'])
    print('expected output:', test['output'])
    print('function output:', result)
    print(result == test['output'])
    end = time.time()
    print('Time taken to execute the function', (end - start))
