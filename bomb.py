class Bomb:
    """
    add description here
    """
    def __init__(self, row, col, radius, time):
        self.__location = (row, col)
        self.__radius = radius
        self.__time = time

    def get_location(self):
        return self.__location