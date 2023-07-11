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


def locate_card_linear(cards, query):
    # Create a variable position with the value 0:
    position = 0

    # set up a loop for repetition:
    while position < len(cards):

        # check if element at the current position matches the query
        if cards[position] == query:
            return position

        # Increment the position if not found
        position += 1

    return -1


large_test_case = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}
start = time.time()
linear_result = locate_card_linear(**large_test_case['input'])
print(linear_result == large_test_case['output'])
end = time.time()
linear_time = (end - start) * 10 ** 3
print('Time taken by Linear Search is :', linear_time, 'ms')

start_1 = time.time()
binary_result = locate_card_binary(**large_test_case['input'])
print(binary_result == large_test_case['output'])
end_1 = time.time()
binary_time = (end_1 - start_1) * 10 ** 3
print('Time taken by Binary Search is :', binary_time, 'ms')
