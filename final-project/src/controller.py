import pygame
from os.path import join
from .settings import *
from pygame.time import get_ticks
from .game import Game
from .preview import Preview
from .score import Score
from .tetrominos import TETROMINOS
from .timer import Timer
from random import choice


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
        

