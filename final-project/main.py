import pygame
from src.game import Game
from src.preview import Preview
from src.score import Score
from src.timer import Timer
from src.tetrominos import TETROMINOS
from src.controller import Controller

from random import choice

# Constants for the Tetris game
COLUMNS = 10
ROWS = 20
BLOCK_SIZE = 40
GAME_WIDTH, GAME_HEIGHT = COLUMNS * BLOCK_SIZE, ROWS * BLOCK_SIZE

SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT = 0.7
SCORE_HEIGHT = 1 - PREVIEW_HEIGHT

PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

UPDATE_SPEED = 800
MOVE_WAIT_TIME = 100
ROTATE_WAIT_TIME = 200
DROP_WAIT_TIME = 400
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# Colors
YELLOW = (255, 213, 0)
RED = (255, 50, 19)
BLUE = (3, 65, 174)
GREEN = (114, 203, 59)
ORANGE = (255, 151, 28)
CYAN = (108, 198, 217)
PURPLE = (123, 33, 127)
GRAY = (28, 28, 28)
LINE_COLOR = (255, 255, 255)

def main():
    pygame.init()
    
    # Create game, preview, and score objects
    game = Game(get_next_shape=lambda: choice(list(TETROMINOS.keys())), update_score=lambda lines, score, level: print(f"Lines: {lines}, Score: {score}, Level: {level}"))
    preview = Preview()
    score = Score()

    # Create the controller
    controller = Controller()

    # Main game loop
    running = True
    while running:
        controller.run()  # Handle input

        # Update game state
        game.run()

        # Update preview and score
        preview.run(next_shapes=["I", "O", "T"])  # Replace with actual upcoming shapes
        score.run()

        # Update display
        pygame.display.update()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
