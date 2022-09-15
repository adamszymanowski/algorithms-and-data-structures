def searching_one_array(array, t):
    """
    Input:  Array of n integers, and t integer
    Output: Whether or not array contains t
    """
    for i in array:
        if i == t:
            return True

    return False

def searching_two_arrays(array_1, array_2, t):
    """
    Input:  Arrays 1 and 2 of n integers each, and an t integer
    Output: Whether or not array 1 or 2 contains t
    """
    for i in array_1:
        if i == t:
            return True

    for i in array_2:
        if i == t:
            return True

    return False

def check_for_common_element(array_1, array_2):
    """
    Input:  Arrays 1 and 2 of n integers each
    Output: Whether or not there is an integer contained in both array 1 and 2
    """
    for i1 in array_1:
        for i2 in array_2:
            if i1 == i2:
                return True

    return False

def check_for_duplicates(array):
    """
    Input:  array of n integers
    """
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[i] == array[j]:
                return True

    return False
