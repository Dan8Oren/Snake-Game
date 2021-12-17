START_ROW = 10
START_COL = 10


class SnakeNode:
    """
    add description here
    """

    def __init__(self, location, next=None, prev=None):
        """

        :param location: the location of the current node - tuple of (row, col)
        :param next:
        """
        self.location = location
        self.next = next
        self.prev = prev


class Snake:
    """
    add description here
    """

    def __init__(self):
        self.__head = self.__tail = None
        self.__length = 0
        self.has_eaten = False
        self.__time_to_grow = 0

    def get_head_location(self):
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
        d = self.__tail.location
        self.__tail = self.__tail.prev
        if self.__tail is None:  # list is now empty
            self.__head = None
        else:  # disconnect old tail
            self.__tail.next.prev = None
            self.__tail.next = None
        self.__length -= 1
        return d

    def create_snake(self, row, col, initial_length):
        """ todo maybe it should be a board method, because there will be games
        todo with snakes that have 4 parts in the beginning
        create a snake in our game
        :param initial_place: in our game, the head of the snake located in
        (10, 10)
        :return: None
        """
        for i in range(initial_length - 1, -1, -1):
            self.add_first((row - i, col))

    def get_snake_cells(self):
        lst_of_cells = []
        if self.__head == None:
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
            return (row + 1, col)
        elif movekey == "Down":
            return (row - 1, col)
        elif movekey == "Left":
            return (row, col - 1)
        elif movekey == "Right":
            return (row, col + 1)

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
        :param prev_move_key: the movekey of the previous move
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
        :param prev_move_key: the movekey of the previous move
        :return: None
        """
        next_head = self.movement_requirements(movekey)
        self.add_first(next_head)

    def update_time(self):
        self.__time_to_grow -= 1
        if self.__time_to_grow == 0:
            self.has_eaten = False

    def set_time_to_grow(self):
        self.__time_to_grow += 3

    def get_length(self):
        return self.__length
