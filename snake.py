START_ROW = 10
START_COL = 10


class SnakeNode:
    """
    add description here
    """

    def __init__(self, location, prev=None, next=None):
        """

        :param location: the location of the current node - tuple of (row,col)
        :param prev:
        :param next:
        """
        self.location = location
        self.prev = prev
        self.next = next


class Snake:
    """
    add description here
    """

    def __init__(self):
        self.__head = self.__tail = None
        self.__length = 0

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

    def add_last(self, location):
        """
        :param location: the location of the new "snake cell"
         to add to the tail .tuple of (row,col)
        :return: None
        """
        node = SnakeNode(location, None, None)
        if self.__tail is None:
            # list was empty
            self.__head = node
        else:  # connect old tail to new node
            self.__tail.next = node
            node.prev = self.__tail
        # update head
        self.__tail = node
        self.__length += 1

    def remove_last(self):
        tail_location = self.__tail.location
        self.__tail = self.__tail.prev
        if self.__tail is None:  # list is now empty
            self.__head = None
        else:  # disconnect old tail
            self.__tail.next.prev = None
        self.__tail.next = None
        self.__length -= 1
        return tail_location

    def create_snake(self, row=START_ROW, col=START_COL):
        """ todo maybe it should be a board method, because there will be games
        todo with snakes that have 4 parts in the beginning
        create a snake in our game
        :param initial_place: in our game, the head of the snake located in
        (10, 10)
        :return: None
        """
        self.add_first((row, col))
        self.add_last((row + 1, col))
        self.add_last((row + 2, col))

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
            return (row - 1, col)
        elif movekey == "Down":
            return (row + 1, col)
        elif movekey == "Left":
            return (row, col - 1)
        elif movekey == "Right":
            return (row, col + 1)

    def possible_move(self, movekey, prev_move_key):
        """
        checks if the user tried to move the snake in the opposite direction
        :param movekey: the current movekey
        :param prev_move_key: the movekey of the previous move
        :return: The legal movekey for the snake to move
        """
        if (movekey == "Up" and prev_move_key == "Down") or (
                movekey == "Down" and prev_move_key == "Up") or (
                movekey == "Left" and prev_move_key == "Right") or (
                movekey == "Right" and prev_move_key == "Left"):
            return prev_move_key
        return movekey

    def move(self, movekey, prev_move_key):
        """
        moves the snake for one turn
        :param movekey: the current movekey
        :param prev_move_key: the movekey of the previous move
        :return: the move the snake did eventually
        """
        move = self.possible_move(movekey, prev_move_key)
        next_head = self.movement_requirements(move)
        self.add_first(next_head)
        self.remove_last()
        return move

    def eat_apple(self, movekey, prev_move_key):
        """
        move the snake for one turn and increase it sizes
        :param movekey: the current movekey
        :param prev_move_key: the movekey of the previous move
        :return: None
        """
        move = self.possible_move(movekey, prev_move_key)
        next_head = self.movement_requirements(move)
        self.add_first(next_head)




# s = Snake()
# s.create_snake()
# print(s.get_snake_cells())
# s.move("Up", "Up")
# print(s.get_snake_cells())
# s.move("Right", "Up")
# print(s.get_snake_cells())
# s.move("Left", "Right")
# print(s.get_snake_cells())
# s.eat_apple("Up", "Left")
# print(s.get_snake_cells())
# s.eat_apple("Down", "Up")
# print(s.get_snake_cells())
