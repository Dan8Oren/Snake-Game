class SnakeNode:
    """
    add description here
    """
    def __init__(self, location, prev = None, next = None):
        """

        :param location: the location of the current node - tuple of (row,col)
        :param prev:
        :param next:
        """
        self.__location = location
        self.__prev = prev
        self.__next = next


class Snake:
    """
    add description here
    """
    def __init__(self, location):
