import game_parameters
from game_display import GameDisplay
import board

NUM_BOMBS = 1
SNAKE_STARTING_LENGTH = 3
NUM_APPLES = 1
POSSIBLE_MOVES = ["Left", "Right", "Up", "Down"]

def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    game_board = board.Board()
    initialize_game(game_board)
    snake_coords = game_board.snake.get_snake_cells()
    play_game = True
    prev_move = "Up"
    while play_game:
        bomb_coords = game_board.bomb.get_location()
        snake_coords = game_board.snake.get_snake_cells()
        play_game = update_display(gd, game_board, bomb_coords, snake_coords)

        key_clicked = gd.get_key_clicked()
        key_clicked = game_board.snake.possible_move(key_clicked,prev_move)
        if key_clicked is None or key_clicked not in POSSIBLE_MOVES:
            prev_move = game_board.snake.move(prev_move)
        else:
            prev_move = game_board.snake.move(key_clicked)

        gd.end_round()


def initialize_game(game_board):
    game_board.add_snake()
    create_bomb(game_board)


def draw_snake(snake_coords, gd):
    for cell in snake_coords:
        gd.draw_cell(cell[1], cell[0], "black")

def create_bomb(game_board):
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = game_board.add_bomb()


def update_display(gd: GameDisplay, game_board, bomb_coords, snake_coords):
    end_game, apple_eaten = game_board.check_snake_move()

    #the game is over: the snake hits himself/the borders/bomb/shockwave
    if end_game:
        draw_snake(snake_coords[1:], gd)
        return True
    else:
        draw_snake(snake_coords, gd)

    # if not game_board.bomb.is_exploded:
    #     gd.draw_cell(bomb_coords[1], bomb_coords[0], "red")
    #     game_board.bomb.update_time()
    # else:
    #     explode, collusion = game_board.bomb.get_explosion(game_board.board)
    #     if collusion:
    #         pass  # TODO: check what is the collusion
    #     if explode:
    #         for shock_coords in explode:
    #             gd.draw_cell(shock_coords[1], shock_coords[0], "orange")
    #     else:
    #         create_bomb(game_board)





if __name__ == '__main__':
    gd = GameDisplay()
    gd.start()






