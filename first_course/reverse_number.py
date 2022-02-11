def reverse_number(number):
    """
    Reverse integer or reverse parts of float number with preserving the sign

    :param number: string to be checked
    :type number: int, float
    :return: Reversed number of same type as input
    :rtype: int, float

    >>> reverse_number(123)
    321
    >>> reverse_number(-100)
    -1
    >>> reverse_number(123.001)
    321.1
    """

    str_input = str(number)
    result = ""
    sign = ""

    if str_input[0] == "-":
        str_input = str_input[1:len(str_input)]
        sign = "-"

    if str_input.count("."):
        int_part = str_input[0:str_input.index(".")]
        float_part = str_input[str_input.index(".") + 1:len(str_input)]
        result += sign + int_part[::-1] + "." + float_part[::-1]
        result = float(result)
    else:
        result += sign + str_input[::-1]
        result = int(result)

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
