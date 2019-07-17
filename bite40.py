def binary_search(t, num):
    '''Search sorted list for element num, return null if not present.
    Implement binary search algorithm.
    '''

    low = 0
    high = len(t) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = t[mid]
        if guess == num:
            return mid
        if guess < num:
            low = mid + 1
        else:
            high = mid - 1
    return None
