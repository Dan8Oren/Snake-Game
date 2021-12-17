import game_parameters as gp
from game_display import GameDisplay
import board

NUM_BOMBS = 1
SNAKE_STARTING_LENGTH = 3
NUM_APPLES = 3
POSSIBLE_MOVES = ["Left", "Right", "Up", "Down"]
START_ROW = 10
START_COL = 10


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)

    game_board = initialize_game()
    is_game_ended = 0
    prev_move = "Up"
    while not is_game_ended:

        key_clicked = gd.get_key_clicked()
        is_game_ended, prev_move = game_board.update_display(key_clicked, prev_move)

        gd.show_score(game_board.get_score())
        game_board.draw(gd, is_game_ended)
        if game_board.get_num_apples() != NUM_APPLES:
            # if there is no room for another apple, game is over
            if game_board.snake.get_length() >= (gp.HEIGHT * gp.WIDTH) - 3:
                is_game_ended = 1
            else:
                create_apples(game_board)
        gd.end_round()



def initialize_game():
    game_board = board.Board(START_COL, START_ROW, SNAKE_STARTING_LENGTH)
    game_board.add_snake()
    create_bomb(game_board)
    create_apples(game_board)

    return game_board


def create_apples(game_board):
    apples_added = game_board.get_num_apples()
    while apples_added != NUM_APPLES:
        result = game_board.add_apple()
        if result:
            apples_added += 1


def create_bomb(game_board):
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = game_board.add_bomb()


# def update_display(gd: GameDisplay, game_board, bomb_coords, snake_coords):
#     end_game, apple_eaten = game_board.check_snake_move()
#
#     #the game is over: the snake hits himself/the borders/bomb/shockwave
#     if end_game:
#         draw_snake(snake_coords[1:], gd)
#         return False
#     else:
#         draw_snake(snake_coords, gd)
#
#     if not game_board.bomb.is_exploded:
#         gd.draw_cell(bomb_coords[1], bomb_coords[0], "red")
#         game_board.bomb.update_time()
#     else:
#         if not game_board.get_bomb_explosion():
#             return False
#
#         else:
#             create_bomb(game_board)





if __name__ == '__main__':
    gd = GameDisplay()
    gd.start()






