

def is_anagram(a, b):
    '''
    Checks if the two words are anagrams, that is, if letters in one word can
    be rearranged to give the other.

    >>> is_anagram('listen', 'silent')
    True
    >>> is_anagram('aabcd', 'dabac')
    True
    >>> is_anagram('cat', 'dog')
    False
    >>> is_anagram('abc', 'defgh')
    False
    >>> is_anagram('abc', 'xbz')
    False
    '''

    a_list = list(a)
    b_list = list(b)

    if sorted(a_list) == sorted(b_list):
        return True
    else:
        return False
