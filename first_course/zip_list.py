def zip_list(some_list: list):
    """
    Converts list of numbers to string.
    Same numbers which are going one by one in the list are
    presented as "3|4" where first number is quantity of second numbers in list ( 4, 4, 4 )
    This values are separated from each other with ":"
    Numbers which are not repeated remain unchanged
    If list contains non-numberic value function returns string "Bad list"
    If argument is not of the type list function returns string "This is not a list"

    :param some_list: List of numbers to be zipped
    :type some_list: list
    :return: Zipped string
    :rtype: str

    >>> zip_list([0, 1, 1, 1, 2, 3, 3, 4, 4, 4, 4])
    "0:3|1:2:2|3:4|4"
    >>> zip_list([0, 1, 2, 3, 4])
    "0:1:2:3:4"
    >>> zip_list([])
    ''
    >>> zip_list([1, 2, 3, 'a', 5])
    'Плохой список'
    >>> # noinspection PyTypeChecker
    ... zip_list((1, 2))
    'Это не список'
    """

    result = ""
    current_number = None
    count = 0

    if type(some_list) != list:
        return "Это не список"

    for number in some_list:
        if type(number) != int:
            return "Плохой список"

        if current_number == number:
            count += 1
        else:
            if count == 1:
                result += f"{current_number}:"
            else:
                result += f"{count}|{current_number}:"
            count = 0

        if count == 0:
            current_number = number
            count += 1

    return result[0:-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
