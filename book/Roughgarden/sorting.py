def merge_sort(array):
    array_length = len(array)

    if array_length <= 1:
        return array
        
    left = []
    right = []
    
    for i, x in enumerate(array):
        if i < array_length//2:
            left.append(x)
        else:
            right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    array = []
    while left and right:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))

    while left:
        array.append(left.pop(0))
    while right:
        array.append(right.pop(0))

    return array

merge_sort([8, 6])