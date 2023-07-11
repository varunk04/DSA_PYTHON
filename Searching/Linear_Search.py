"""
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""
import time


def locate_card_linear(cards, query):
    # Create a variable position with the vakue 0:
    position = 0

    # set up a loop for repetition:
    while position < len(cards):

        # check if element at the current position matches the query
        if cards[position] == query:
            return position

        # Increment the position if not found
        position += 1

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
    }
]

for test in tests:
    start = time.time()
    result = locate_card_linear(**test['input'])
    print('input :', test['input'])
    print('expected output:', test['output'])
    print('function output:', result)
    print(result == test['output'])
    end = time.time()
    print('Time taken to execute the function', (end - start) * 10 ** 3, 'ms')
