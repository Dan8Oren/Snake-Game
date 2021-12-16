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
    bomb_coords = game_board.bomb.get_location()
    snake_coords = game_board.snake.get_snake_cells()
    play_game = True
    prev_move = "Up"
    while play_game:
        key_clicked = gd.get_key_clicked()
        key_clicked = game_board.snake.possible_move(key_clicked,prev_move)
        if key_clicked in POSSIBLE_MOVES:
            prev_move = game_board.snake.move(key_clicked,prev_move)
            snake_coords = game_board.snake.get_snake_cells()
        # elif (key_clicked == 'Right'):
        #     prev_move = game_board.snake.move(key_clicked,prev_move)
        # elif (key_clicked == 'Up'):
        #     prev_move = key_clicked
        #     snake_coords[1] += 1
        # elif (key_clicked == 'Down'):
        #     prev_move = key_clicked
        #     snake_coords[1] -= 1True

        update_display(gd, game_board)
        draw_snake(snake_coords, gd)
        gd.end_round()



def initialize_game(game_board):
    game_board.add_snake()
    create_bomb(game_board)

def draw_snake(snake_coords, gd):
    for cell in snake_coords:
        gd.draw_cell(cell[0], cell[1], "black")

def create_bomb(game_board):
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = game_board.add_bomb()


def update_display(gd: GameDisplay, game_board):
    bomb_coords = game_board.bomb.get_location()
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






