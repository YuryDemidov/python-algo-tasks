def unzip_list(zipped_list: list):
    """
    The zipped list is considered to be list of values of type "2|4".
    The first number represents the number of repeats of second number
    The function convert this type of values and returns the list of plain row of numbers
    If list contains value without | which could be of number type it should be added to final list
    If list contains non-numberic value function returns string "Bad list"
    If argument is not of the type list function returns string "This is not a list"

    :param zipped_list: Zipped list to be processed
    :type zipped_list: list
    :return: Unzipped list
    :rtype: list

    >>> unzip_list(["1|2", "3|4"])
    [2, 4, 4, 4]
    >>> unzip_list(["1|4", "2|5", "10|1"])
    [4, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> unzip_list(["1|4", "2"])
    [4, 2]
    >>> unzip_list([])
    []
    >>> unzip_list([1, 2, 3, 'a', 5])
    'Плохой список'
    >>> # noinspection PyTypeChecker
    ... unzip_list((1, 2))
    'Это не список'
    """

    result = []

    if type(zipped_list) != list:
        return 'Это не список'

    for value in zipped_list:
        if type(value) != str:
            return 'Плохой список'

        if value.isdigit():
            result.append(int(value))
        else:
            separator_index = value.find("|")
            if separator_index == -1:
                return 'Плохой список'

            for i in range(int(value[0:separator_index])):
                result.append(int(value[separator_index + 1:]))

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
