import game
import game_parameters as gp
from game_display import GameDisplay

NUM_BOMBS = 1
SNAKE_STARTING_LENGTH = 3
NUM_APPLES = 3
POSSIBLE_MOVES = ["Left", "Right", "Up", "Down"]
START_ROW = 10
START_COL = 10


def main_loop(gd: GameDisplay) -> None:
    """
    The main function that plays the game
    :param gd: GameDisplay object
    :return: None
    """
    gd.show_score(0)

    snake_game = initialize_game()
    is_game_ended = 0
    snake_game.draw(gd, is_game_ended)
    gd.end_round()
    prev_move = "Up"
    while not is_game_ended:
        key_clicked = gd.get_key_clicked()
        is_game_ended, prev_move = snake_game.update_display(key_clicked,
                                                             prev_move)
        gd.show_score(snake_game.get_score())

        if snake_game.get_num_apples() != NUM_APPLES:
            # if there is no room for another apple, game is over
            if snake_game.snake.get_length() >= (gp.HEIGHT * gp.WIDTH) - 3:
                is_game_ended = 2
            else:
                create_apples(snake_game)
        if not snake_game.bomb:
            # if there is no room for a new bomb, game is over
            if snake_game.snake.get_length() >= (gp.HEIGHT * gp.WIDTH) - 3:
                is_game_ended = 2
            else:
                create_bomb(snake_game)

        snake_game.draw(gd, is_game_ended)
        gd.end_round()


def initialize_game():
    """
    creates all game objects according the parameters decided.
    :return: snake Game object
    """
    snake_game = game.Game(START_COL, START_ROW, SNAKE_STARTING_LENGTH)
    snake_game.add_snake()
    create_bomb(snake_game)
    create_apples(snake_game)

    return snake_game


def create_apples(snake_game):
    """
    adds apples to the game
    :param snake_game: a game object
    :return: None
    """
    apples_added = snake_game.get_num_apples()
    while apples_added != NUM_APPLES:
        result = snake_game.add_apple()
        if result:
            apples_added += 1


def create_bomb(snake_game):
    """
    creates a new __bomb in game
    :param snake_game: current game board
    :return: None
    """
    is_bomb_created = False
    while not is_bomb_created:
        is_bomb_created = snake_game.add_bomb()


if __name__ == '__main__':
    gd = GameDisplay()
    gd.start()
