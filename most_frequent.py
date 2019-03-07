

def most_frequent(numbers):
    '''
    Check what is the most frequent number in an array.
    If there are multiple such numbers, return the largest one.

    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4])
    3
    >>> most_frequent([3, 3, 3, 2, 2, 2, 4, 4, 4, 4])
    4
    >>> most_frequent([3, 6, 3, 3, 6, 2, 2, 6, 2, 4, 4])
    6
    >>> most_frequent([3, 6, 2, 6, 5, 6, 9, 9, 9, 10, 9])
    9
    '''

    frequention = {}

    for k in numbers:
        if k not in frequention.keys():
            frequention[k] = 1
        else:
            frequention[k] += 1
    
    fre = [[i[0], i[1]] for i in frequention.items()]
    most = max([(i[1], i[0]) for i in fre])
    # for i in range(len(fre)):
    return most[1]


print(most_frequent([3, 6, 2, 6, 5, 6, 9, 9, 9, 10, 9]))
