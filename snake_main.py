import game_parameters
from game_display import GameDisplay
import board

NUM_BOMBS = 1
SNAKE_STARTING_LENGTH = 3
NUM_APPLES = 1
POSSIBLE_MOVES = ["Left", "Right", "Up", "Down"]
START_ROW = 10
START_COL = 10

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)

    game_board = initialize_game()
    game_board.draw()
    snake_coords = game_board.snake.get_snake_cells()
    play_game = True
    prev_move = "Up"
    while play_game:
        bomb_coords = game_board.bomb.get_location()
        snake_coords = game_board.snake.get_snake_cells()
        # play_game = update_display(gd, game_board, bomb_coords, snake_coords)

        key_clicked = gd.get_key_clicked()
        check_input(key_clicked)
        play_game,prev_move = game_board.update_display(key_clicked,prev_move)
        game_board.draw()

        gd.end_round()


def check_input(key_clicked):
    pass


def initialize_game(game_board):
    game_board = board.Board(START_ROW,START_COL)
    game_board.add_snake()
    create_bomb(game_board)
    #TODO: Apples

    return game_board


def create_bomb(game_board):
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = game_board.add_bomb()


def update_display(gd: GameDisplay, game_board, bomb_coords, snake_coords):
    end_game, apple_eaten = game_board.check_snake_move()

    #the game is over: the snake hits himself/the borders/bomb/shockwave
    if end_game:
        draw_snake(snake_coords[1:], gd)
        return False
    else:
        draw_snake(snake_coords, gd)

    if not game_board.bomb.is_exploded:
        gd.draw_cell(bomb_coords[1], bomb_coords[0], "red")
        game_board.bomb.update_time()
    else:
        if not game_board.get_bomb_explosion():
            return False

        else:
            create_bomb(game_board)





if __name__ == '__main__':
    gd = GameDisplay()
    gd.start()






