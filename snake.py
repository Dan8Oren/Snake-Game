START_ROW = 10
START_COL = 10


class SnakeNode:
    """
    a class that represents s single cell in the snake's "body"
    """

    def __init__(self, location, next=None, prev=None):
        """

        :param location: the location of the current node - tuple of (row, col)
        :param next: a pointer to the next cell
        :param prev: a pointer to the previous cell
        """
        self.location = location
        self.next = next
        self.prev = prev


class Snake:
    """
    This class represents a snake. The snake is a doubly linked list.
    This class has all the methods to change and update the snake's attributes
    """

    def __init__(self):
        self.__head = self.__tail = None
        self.__length = 0
        self.has_eaten = False
        self.__time_to_grow = 0

    def get_head_location(self):
        """
        :return: the location of the head of the snake
        """
        return self.__head.location

    def add_first(self, location):
        """
        :param location: the location of the new "snake cell"
         to add to the head .tuple of (row,col)
        :return: None
        """
        node = SnakeNode(location, None, None)
        if self.__head is None:
            # list was empty
            self.__tail = node
        else:  # connect old head to new node
            self.__head.prev = node
            node.next = self.__head
        # update head
        self.__head = node
        self.__length += 1

    def remove_last(self):
        """
        remove the tail of the snail
        :return: None
        """
        self.__tail = self.__tail.prev
        if self.__tail is None:  # list is now empty
            self.__head = None
        else:  # disconnect old tail
            self.__tail.next.prev = None
            self.__tail.next = None
        self.__length -= 1

    def create_snake(self, row, col, initial_length):
        """
        create a snake in our game
        :param initial_length: in our game, the head of the snake located in
        (10, 10)
        :param col: starting column of the snake's position
        :param row: starting row of the snake's position
        :return: None
        """
        for i in range(initial_length - 1, -1, -1):
            self.add_first((row - i, col))

    def get_snake_cells(self):
        lst_of_cells = []
        if self.__head is None:
            return []
        cur = self.__head
        while cur:
            lst_of_cells.append(cur.location)
            cur = cur.next

        return lst_of_cells

    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A cell which must be empty in order for this move to be legal.
        """
        row, col = self.get_head_location()
        if movekey == "Up":
            return row + 1, col
        elif movekey == "Down":
            return row - 1, col
        elif movekey == "Left":
            return row, col - 1
        elif movekey == "Right":
            return row, col + 1

    def possible_move(self, movekey, prev_move_key):
        """
        checks if the user tried to move the snake in the opposite direction
        or if he doesn't enter anything(None)
        :param movekey: the current movekey
        :param prev_move_key: the movekey of the previous move
        :return: The legal movekey for the snake to move
        """
        if movekey is None:
            return prev_move_key

        if (movekey == "Up" and prev_move_key == "Down") or (
                movekey == "Down" and prev_move_key == "Up") or (
                movekey == "Left" and prev_move_key == "Right") or (
                movekey == "Right" and prev_move_key == "Left"):
            return prev_move_key
        return movekey

    def move(self, movekey):
        """
        moves the snake for one turn
        :param movekey: the current movekey
        :return: the move the snake did eventually
        """
        next_head = self.movement_requirements(movekey)
        self.add_first(next_head)
        self.remove_last()
        return movekey

    def eat_apple_movement(self, movekey):
        """
        move the snake for one turn and increase it sizes
        :param movekey: the current movekey
        :return: None
        """
        next_head = self.movement_requirements(movekey)
        self.add_first(next_head)

    def update_time(self):
        """
        calculates the number of turns for the snake to increase its size
        :return: None
        """
        self.__time_to_grow -= 1
        if self.__time_to_grow == 0:
            self.has_eaten = False

    def set_time_to_grow(self):
        """
        if a snake ate an apple, it will grow for 3 turns
        :return: None
        """
        self.__time_to_grow += 3

    def get_length(self):
        """
        :return: the length of the snake
        """
        return self.__length
