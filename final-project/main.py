import pygame
from src.controller import Controller

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
