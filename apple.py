class Apple:
    """
    Represents the apples in snake game, each apples has a location on board
    and a score
    """

    def __init__(self, row, col, score):
        self.__location = (row, col)
        self.__score = score

    def get_location(self):
        """
        :return: Apples location
        """
        return self.__location

    def get_score(self):
        """
        :return: The apple score
        """
        return self.__score

    def __str__(self):  # TODO delete?
        row, col = self.__location[0], self.__location[1]
        return f"row is: {row}, col is: {col}"
