import game_parameters
from game_display import GameDisplay
import board

NUM_BOMBS = 1
SNAKE_STARTING_LENGTH = 3
NUM_APPLES = 1


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    game_board = board.Board()
    initialize_game(game_board)
    bomb_coords = game_board.bomb.get_location()
    snake_coords = [10, 10]
    play_game = True
    while play_game:
        key_clicked = gd.get_key_clicked()
        if (key_clicked == 'Left') and (snake_coords[0] > 0):
            snake_coords[0] -= 1
        elif (key_clicked == 'Right') and (snake_coords[0] < game_parameters.WIDTH):
            snake_coords[0] += 1
        elif (key_clicked == 'Up'):
            snake_coords[1] += 1
        elif (key_clicked == 'Down'):
            snake_coords[1] -= 1
            game_board.bomb.is_exploded = True

        update_display(gd, game_board)
        gd.draw_cell(snake_coords[0], snake_coords[1], "black")
        gd.end_round()


def initialize_game(game_board):
    create_bomb(game_board)


def create_bomb(game_board):
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = game_board.add_bomb()


def update_display(gd: GameDisplay, game_board):
    bomb_coords = game_board.bomb.get_location()
    snake_coords = [10, 10]
    gd.draw_cell(bomb_coords[0], bomb_coords[1], "red")
    if not game_board.bomb.end_bomb:
        if game_board.bomb.is_exploded:
            explode, collusion = game_board.bomb.get_explosion(game_board.board)
            if collusion:
                pass  # TODO: check what is the collusion
            for shock_coords in explode:
                gd.draw_cell(shock_coords[0], shock_coords[1], "orange")
    else:
        create_bomb(game_board)


if __name__ == '__main__':
    gd = GameDisplay()
    gd.start()






