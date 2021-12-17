import game_parameters as gp
from apple import Apple
from game_bomb import Bomb
from snake import Snake

SNAKE = "black"
BOMB = "red"
APPLE = "green"
SHOCK_WAVE = "orange"
ALL_GOOD = 0
WRONG_HEAD_MOVE = 1
WRONG_BODY_MOVE = 2


class Game:
    """
    The class Game,is the class that controls all Snake's objects, updates them
    according the player choices and displays them to the player,
    using Game Display objects. TODO: maybe rewrite
    """

    def __init__(self, snake_col, snake_row, snake_initial_length):
        # A Dictionary! key:Tuple of coords, value:Apple class object
        self.__lst_of_apples = {}  # ^^info^^
        self.bomb = None
        self.__bomb_prints = []
        self.snake = None
        self.snake_initial_length = snake_initial_length
        self.__snake_start = (snake_row, snake_col)
        self.__height = gp.HEIGHT
        self.__width = gp.WIDTH
        self.__score = 0

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the object in coordinate, None if empty
        """
        if coordinate in self.__bomb_prints:
            return BOMB
        if coordinate in self.__lst_of_apples:
            return APPLE
        if coordinate in self.snake.get_snake_cells():
            return SNAKE
        return None

    def update_score(self, apple_score):
        """
        Updates game score
        :param apple_score: how many points should be added to score
        :return: updated game score
        """
        self.__score += apple_score

    def get_score(self):
        """
        :return: current game score
        """
        return self.__score

    def add_apple(self):
        """
        Adds an apple to the board.
        :return: True upon success. False if failed
        """
        col, row, score = gp.get_random_apple_data()
        if not 0 <= row < self.__height and 0 <= col < self.__width:
            return False
        # if a cell in the board already has apple/bomb/snake/shockwave
        if self.cell_content((row, col)):
            return False
        apple = Apple(row, col, score)
        self.__lst_of_apples[(row, col)] = apple
        return True

    def get_num_apples(self):
        """
        :return: number of apples currently in the game
        """
        return len(self.__lst_of_apples)

    def add_bomb(self):
        """
        Adds a bomb to the board.
        :return: True upon success. False if failed
        """
        col, row, radius, time = gp.get_random_bomb_data()

        if not 0 <= row < self.__height and 0 <= col < self.__width:
            return False
        # if a cell in the board already has apple/bomb/snake/shockwave
        if self.cell_content((row, col)):
            return False
        self.bomb = Bomb(row, col, radius, time)
        self.__bomb_prints.append((row, col))
        return True

    def add_snake(self):
        """
        Adds a snake to the game
        :return: None
        """
        self.snake = Snake()
        self.snake.create_snake(self.__snake_start[0], self.__snake_start[1],
                                self.snake_initial_length)

    def check_snake_move(self):
        """

        :return: A tuple which contains:
        first value: True if the movement of the snake will lead to ending
        the game. False upon success
        second Value: True if the snake ate an apple, else False
        """
        head_location = self.snake.get_head_location()  # (row, col)
        snake_cells = self.snake.get_snake_cells()

        # if the snake hits himself
        if head_location in snake_cells[1:]:
            return WRONG_HEAD_MOVE

        # if the snake crushes into the borders of the board
        if head_location[0] < 0 or head_location[0] >= gp.HEIGHT or \
                head_location[1] < 0 or head_location[1] >= gp.WIDTH:
            return WRONG_HEAD_MOVE

        # if the snake hits a bomb/shockwave
        if self.cell_content(head_location) == BOMB:
            return WRONG_HEAD_MOVE

        # if the snake hits a shockwave
        for cell in snake_cells:
            if self.cell_content(cell) == BOMB:
                return WRONG_BODY_MOVE

        # if the snake ate an apple, act accordingly
        if self.cell_content(head_location) == APPLE:
            self.snake_eats_apple(head_location)

        return ALL_GOOD

    def snake_eats_apple(self, apple_location):
        """
        This function performs all the actions to be done when a snake eats an
        apple: the snake will grow, the score of the apple is added to the
        score of the game, the apple will be deleted from the game
        :param apple_location: the location of an apple
        :return: None
        """
        self.snake.has_eaten = True
        self.snake.set_time_to_grow()
        apple_score = self.__lst_of_apples[apple_location].get_score()
        self.update_score(apple_score)
        del self.__lst_of_apples[apple_location]

    def draw(self, gd, game_status):
        """
        Draws the game according to current game objects status
        :param gd: Game_Display object
        :param game_status:
        0 if the game can continue
        1 if the head of the snake got stuck in himself/the borders
        2 if a bomb/shockwave hits the snake
        :return: None
        """
        snake_cells = self.snake.get_snake_cells()
        if game_status == WRONG_HEAD_MOVE:
            for cell in snake_cells[1:]:
                gd.draw_cell(cell[1], cell[0], SNAKE)
        else:
            for cell in snake_cells:
                gd.draw_cell(cell[1], cell[0], SNAKE)
        if self.bomb.is_exploded():
            for cell in self.__bomb_prints:
                gd.draw_cell(cell[1], cell[0], SHOCK_WAVE)
        else:
            b_loc = self.bomb.get_location()
            gd.draw_cell(b_loc[1], b_loc[0], BOMB)

        for apple in self.__lst_of_apples:
            gd.draw_cell(apple[1], apple[0], APPLE)

    def update_display(self, key_clicked, prev_move):
        """
        changes all game objects according to user input
        :param key_clicked: A key the player pressed
        :param prev_move: previous snake move
        :return: Tuple of (boolean,string),
        Boolean: True to keep playing, False otherwise
        String: the snake move in this round
        """
        self.bomb.update_time()
        if self.bomb.is_exploded():
            self.get_bomb_explosion()

        key_clicked = self.snake.possible_move(key_clicked, prev_move)
        if self.snake.has_eaten:
            self.snake.eat_apple_movement(key_clicked)
            self.snake.update_time()
        else:
            self.snake.move(key_clicked)

        is_game_ended = self.check_snake_move()
        return is_game_ended, key_clicked

    def get_bomb_explosion(self):
        """
        Gets the bomb explosion radius, checks collusion with apples
        :return: None
        """
        width = self.__width
        height = self.__height
        shock_wave, collusion = self.bomb.get_explosion(self, width, height)
        self.__bomb_prints = []
        if shock_wave:
            if collusion:
                for ram in collusion:
                    cell = self.cell_content(ram)
                    self.__bomb_prints.append(ram)
                    if cell == APPLE:
                        del self.__lst_of_apples[ram]

            for coord in shock_wave:  # maybe change the order of the print
                self.__bomb_prints.append(coord)
        else:
            self.create_new_bomb()

    def create_new_bomb(self):
        """
        creates new bomb in Game
        :return: None
        """
        self.__bomb_prints = []
        result = False
        while not result:
            result = self.add_bomb()
