# src/controller.py
import pygame
from os.path import join
from pygame.time import get_ticks
from .game import Game
from .preview import Preview
from .score import Score
from .tetrominos import TETROMINOS
from .timer import Timer
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

# shapes
TETROMINOS = {
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': PURPLE},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': YELLOW},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': BLUE},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': ORANGE},
	'I': {'shape': [(0,0), (0,-1), (0,-2), (0,1)], 'color': CYAN},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': GREEN},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': RED}
}


class Controller:
    def __init__(self):
        # General setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # Shapes
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

        # Components
        self.game = Game(self.get_next_shape, self.update_score)
        self.score = Score()
        self.preview = Preview()

        # Game state
        self.paused = False

        # Font for the pause menu
        self.font = pygame.font.Font(join('final-project', 'assets','font','NotoSans-Regular.ttf'), 40)

    def update_score(self, lines, score, level):
        self.score.lines = lines
        self.score.score = score
        self.score.level = level

    def get_next_shape(self):
        next_shape = self.next_shapes.pop(0)
        self.next_shapes.append(choice(list(TETROMINOS.keys())))
        return next_shape

    def draw_pause_menu(self):
        """Display the pause menu."""
        pause_text = self.font.render("PAUSED", True, "white")
        resume_text = self.font.render("Press 'P' to Resume", True, "white")
        
        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        resume_rect = resume_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        self.display_surface.blit(pause_text, pause_rect)
        self.display_surface.blit(resume_text, resume_rect)
    
    def restart_game(self):
        """Restart the game by reinitializing components."""
        self.game = Game(self.get_next_shape, self.update_score)
        self.next_shapes = [choice(list(TETROMINOS.keys())) for shape in range(3)]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.paused = not self.paused  # Toggle pause state
                if self.game.game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.restart_game()

            if self.paused:
                # Display pause menu
                self.display_surface.fill(GRAY)
                self.draw_pause_menu()
            elif self.game.game_over:
                self.game.display_game_over()
            else:
                # Normal game rendering
                self.display_surface.fill(GRAY)

                # Components
                self.game.run()
                self.score.run()
                self.preview.run(self.next_shapes)


            # Update the screen
            pygame.display.update()
            self.clock.tick(60)
        

