import game_parameters as gp
from apple import Apple
from game_bomb import Bomb
from snake import Snake

SNAKE = "s"
BOMB = "b"
APPLE = "a"
SHOCK_WAVE = "s"
START_ROW = 10
START_COL = 10


class Board:
    """
    add description here
    """

    def __init__(self):
        self.board = [[None for _ in range(gp.WIDTH)] for _ in
                        range(gp.HEIGHT)]
        self.__lst_of_apples = []
        self.bomb = None
        self.snake = None

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the object in coordinate, None if empty
        """
        return self.board[coordinate[0]][coordinate[1]]

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
        self.board[row][col] = APPLE
        return True

    def add_bomb(self):
        """
        Adds a bomb to the board.
        :return: True upon success. False if failed
        """
        # TODO: row/col is opposite!?
        row,col,radius, time = gp.get_random_bomb_data()

        if not 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
            return False
        # if a cell in the board already has apple/bomb/snake/shockwave
        if self.cell_content((row, col)):
            return False
        self.bomb = Bomb(row, col, radius, time)
        self.board[row][col] = BOMB
        return True

    def add_snake(self):
        """
        Adds a snake to the game
        :return: None
        """
        self.snake = Snake()
        self.snake.create_snake(START_ROW, START_COL)
        s_cords = self.snake.get_snake_cells()
        for cell in s_cords:
            self.board[cell[0]][cell[1]] = SNAKE

    def move_snake(self, movekey, prev_move_key):
        """
        :return:
        """
        pass

    def check_snake_move(self):
        """

        :return: A tuple which contains:
        first value: True if the movement of the snake will lead to ending
        the game. False upon success
        second Value: True if the snake ate an apple, else False
        """
        head_location = self.snake.get_head_location()
        snake_cells = self.snake.get_snake_cells()

        # if the snake hits himself
        if head_location in snake_cells[1:]:
            return True, False

        # if the snake crushes into the borders of the board
        if head_location[0] < 0 or head_location[0] >= len(self.board) or \
                head_location[1] < 0 or head_location[1] >= len(self.board[0]):
            return True, False

        # if the snake hits a bomb
        if self.cell_content(head_location) == BOMB:
            return True, False

        # if the snake hits the shockwave of a bomb
        #todo !!!!!!!!!!!!!!!!!
        if ...:
            return True, False

        # if the snake ate an apple, act accordingly
        if self.cell_content(head_location) == APPLE:
            pass  #  todo!!!!!!!!!!!!!!1


    def get_bomb_explosion(self):
        width = len(self.board[0])
        height = len(self.board)
        shock_wave,collusion = self.bomb.get_explosion(self,width,height)
        if shock_wave:
            if collusion:
                for ram in collusion:
                    cell = self.cell_content(ram)
                    if cell == APPLE:
                        self.board[ram[0]][ram[1]] = SHOCK_WAVE
                    else:
                        return False
            else:
                for coord in shock_wave:
                    self.board[coord[0]][coord[1]] = SHOCK_WAVE
        else:
            self.add_bomb()
        return True

    def __str__(self):
        st = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if not self.board[i][j]:
                    st += "_\t"
                else:
                    st += (self.board[i][j] + "\t")
            st += "\n"
        return st
