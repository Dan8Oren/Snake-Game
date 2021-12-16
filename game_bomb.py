import game_display as gp

class Bomb:
    """
    add description here
    """

    def __init__(self, row, col, radius, time):
        self.__location = (row, col)
        self.__radius = [num for num in range(radius - 1, -1, -1)]
        self.__time = time
        self.__is_exploded = False

    def get_location(self):
        """
        gets the bomb location
        returns: tuple of row,col coordinates
        """
        return self.__location

    def get_explosion(self,board,board_width,board_hight):
        """
        gets the specific radius coordinates of a bomb explosion,
        updates the bomb status to exploded, updates if the bomb should be
        relocated (end_bomb)
        :param board: current board (only using it's size)
        returns: list of explosion coordinates,
         collusion coordinates and a boolean if bomb should get a new location
        """
        self.__is_exploded = True
        if self.__radius:
            radius = self.__radius.pop()
        else:
            return None  # Shouldn't happen
        if not self.__radius:
            self.end_bomb = True
        if radius == 0:
            return [self.__location], None

        explosion_coordinates = []
        collusion_coordinates = []
        start_row = 0
        start_col = 0
        b_row = self.__location[0]
        b_col = self.__location[1]
        if 0 <= b_row - radius < board_hight:
            start_row = b_row - radius
        if 0 <= b_col - radius < board_width:
            start_col = b_col - radius
        for row in range(start_row, start_row + (2 * radius) + 1):
            for col in range(start_col, start_col + (2 * radius) + 1):
                if abs(b_col - col) + abs(b_row - row) == radius:
                    explosion_coordinates.append((row, col))
                    if 0 <= row < board_hight and 0 <= col < board_width:
                        explosion_coordinates.append((row, col))
                        if board.cell_content((row, col)):  # TODO: what should happen?
                            collusion_coordinates.append((row, col))
                    else:
                        break
                        # TODO: should make a new bomb in a new location
            else:
                return explosion_coordinates, collusion_coordinates
        return [], []


    def update_time(self):
        self.__time -= 1
        if self.__time == 0:
            self.__is_exploded = True
