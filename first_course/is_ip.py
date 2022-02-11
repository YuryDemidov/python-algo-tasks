def is_ip(string: str):
    """
    Checks that passed string is a valid IP-address

    :param string: string to be checked
    :type string: str
    :return: True if string is a valid IP and False if it is not
    :rtype: bool

    >>> is_ip("127.22.0.255")
    True
    >>> is_ip("256.22.0.100")
    False
    >>> is_ip("127.22.0.")
    False
    >>> is_ip("")
    False
    >>> is_ip("Text")
    False
    >>> # noinspection PyTypeChecker
    ... is_ip(127060345)
    False
    """

    if type(string) != str:
        return False

    ip_parts = string.split(".")

    if len(ip_parts) != 4:
        return False

    for part in ip_parts:
        if not part.isdecimal():
            return False
        if not 0 <= int(part) < 256:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
