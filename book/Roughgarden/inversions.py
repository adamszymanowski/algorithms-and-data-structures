def brute_force_count_inversions(array):
    inversions = 0
    n = len(array)
    for i in range(n-1):
        for j in range(i+1, n):
            if array[i] > array[j]:
                inversions = inversions + 1

    return inversions