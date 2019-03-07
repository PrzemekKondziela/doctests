

def poker_hand(hand):
    '''
    Function score a poker hand. The function take an array 5 numbers and return a string based on what is inside.

    >>> poker_hand([1, 1, 1, 1, 1])
    'five'
    >>> poker_hand([2, 2, 2, 2, 3])
    'four'
    >>> poker_hand([1, 1, 1, 2, 3])
    'three'
    >>> poker_hand([2, 2, 3, 3, 4])
    'twopairs'
    >>> poker_hand([1, 2, 2, 3, 4])
    'pair'
    >>> poker_hand([1, 1, 2, 2, 2])
    'fullhouse'
    >>> poker_hand([1, 2, 3, 4, 6])
    'nothing'
    '''

    cards = {}

    for k in hand:
        if k not in cards.keys():
            cards[k] = 1
        else:
            cards[k] += 1

    frequency = [[i[0], i[1]] for i in cards.items()]

    set_on_hand = []

    for i in range(len(frequency)):
        set_on_hand.append(frequency[i][1])

    set_on_hand.sort(reverse=True)

    rank = ("five", 'four', 'three', 'twopairs', 'pair', 'fullhouse', 'nothing')
    if set_on_hand == [5]:
        return rank[0]
    elif set_on_hand == [4, 1]:
        return rank[1]
    elif set_on_hand == [3, 1, 1]:
        return rank[2]
    elif set_on_hand == [2, 2, 1]:
        return rank[3]
    elif set_on_hand == [2, 1, 1, 1]:
        return rank[4]
    elif set_on_hand == [3, 2]:
        return rank[5]
    else:
        return rank[6]
