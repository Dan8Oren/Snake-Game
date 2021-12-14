import game_parameters as gp
from apple import Apple
from bomb import Bomb

SNAKE = "s"
BOMB = "b"
APPLE = "a"

class Board:
    """
    add description here
    """
    def __init__(self):
        self.__board = [[None for _ in range(gp.WIDTH)] for _ in range(gp.HEIGHT)]
        self.__lst_of_apples = []
        self.__bomb = None
        self.__snake = None

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the object in coordinate, None if empty
        """
        return self.__board[coordinate[0]][coordinate[1]]

    def add_apple(self):
        """
        Adds an apple to the board.
        :return: True upon success. False if failed
        """
        col, row, score = gp.get_random_apple_data()

        # if a cell in the board already has apple/bomb/snake/shockwave
        if self.cell_content((row, col)):
            return False
        apple = Apple(row, col, score)
        self.__lst_of_apples.append(apple)
        self.__board[row][col] = APPLE
        return True

    def add_bomb(self):
        """
        Adds a bomb to the board.
        :return: True upon success. False if failed
        """
        col, row, radius, time = gp.get_random_bomb_data()

        # if a cell in the board already has apple/bomb/snake/shockwave
        if self.cell_content((row, col)):
            return False

        self.__bomb = Bomb(row, col, radius, time)
        self.__board[row][col] = BOMB
        return True


    def __str__(self):
        st = ""
        for i in range(len(self.__board)):
            for j in range(len(self.__board[0])):
                if not self.__board[i][j]:
                    st += "_\t"
                else:
                    st += (self.__board[i][j]+"\t")
            st += "\n"
        return st


b= Board()
print(b)
b.add_apple()
b.add_bomb()
b.add_bomb()
b.add_bomb()
print(b)

