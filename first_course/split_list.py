def split_list(some_list: list, divider):
    """
    Divides the original list into two by the first occurrence of the divider
    Returns original list without changes if divider is not present in list

    :param some_list: original list
    :type some_list: list
    :param divider: item of the list which will be used for dividing of original list
    :return: tuple of lists
    :rtype: tuple

    >>> split_list([1, 2, 3, 4, 5, 6, 7], 4)
    ([1, 2, 3], [5, 6, 7])
    >>> split_list([1, 2, 3, 4, 5, 6, 7], 8)
    [1, 2, 3, 4, 5, 6, 7]
    >>> split_list([1, 2, 3, 4, 5, 6, 7], 7)
    ([1, 2, 3, 4, 5, 6], [])
    >>> # noinspection PyTypeChecker
    ... split_list((12345, 1), 6)
    'Это не список'
    """

    if type(some_list) != list:
        return 'Это не список'
    if some_list.count(divider) == 0:
        return some_list

    result = ([], [])
    divider_position = some_list.index(divider)
    for i in range(0, len(some_list)):
        if i < divider_position:
            result[0].append(some_list[i])
        elif i > divider_position:
            result[1].append(some_list[i])
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
