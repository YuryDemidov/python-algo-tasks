def running_sum(some_list: list):
    """
    Calculates cummulative sum of list of numbers
    (the sum where next term should be added to total sum and return his own intermediate sum)
    If list contains uncountable value function returns string "Bad list"
    If argument is not of the type list function returns string "This is not a list"

    :param some_list: List of values to calculate
    :type some_list: list
    :return: List of cummulative sum (sum for each element of original list)
    :rtype: list

    >>> running_sum([1, 1, 1, 1, 1])
    [1, 2, 3, 4, 5]
    >>> running_sum([1, 2, 3, 4, 5])
    [1, 3, 6, 10, 15]
    >>> running_sum([11])
    [11]
    >>> running_sum([])
    []
    >>> running_sum([1, 2, 3, 'a', 5])
    'Плохой список'
    >>> # noinspection PyTypeChecker
    ... running_sum((1, 2))
    'Это не список'
    """

    result = []
    cumulative_sum = 0

    if type(some_list) != list:
        return "Это не список"

    for value in some_list:
        if type(value) != int and type(value) != float:
            return "Плохой список"
        cumulative_sum += value
        result.append(cumulative_sum)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
