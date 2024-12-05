import pygame
from src.settings import *
from src.game import Game
from src.preview import Preview
from src.score import Score
from src.timer import Timer
from src.tetrominos import TETROMINOS
from src.controller import Controller
from random import choice



def main():
    pygame.init()

    # Create the controller
    controller = Controller()

    # Main game loop
    running = True
    while running:
        controller.run()
        # Update game state
        game.run()

        # Update preview and score
        preview.run()
        score.run()

        # Update display
        pygame.display.update()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
