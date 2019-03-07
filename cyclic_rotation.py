

def cyclic_rotation(word, n):
    '''
    Calculate a cyclic rotation of a string;
     i.e. move the last N elements from the end to the beginning.

     >>> cyclic_rotation('abcde', 2)
     'deabc'
    >>> cyclic_rotation('warszawa', 4)
    'zawawars'
    >>> cyclic_rotation('babababa', 3)
    'abababab'
    '''

    for i in range(len(word)):
        a = word[(-n):] + word[:(-n)]
    return a
