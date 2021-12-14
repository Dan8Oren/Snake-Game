class Apple:
    """
    add description here
    """
    def __init__(self, row, col, score):
        self.__location = (row, col)
        self.__score = score

    def get_location(self):
        return self.__location

    def __str__(self):
        row, col = self.__location[0], self.__location[1]
        return f"row is: {row}, col is: {col}"
