def sum_numbers(numbers=None):
    """Write a function that can sum up numbers:

    It should receive a list of n numbers.
    If no argument is provided, return sum of numbers 1..100.
    """
    if numbers == None:
        return sum(range(1, 101))
    return sum(numbers)
