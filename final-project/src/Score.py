# src/score.py
import pygame
from os.path import join

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

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}

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

class Score:
	def __init__(self):
		self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT - PADDING))
		self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING,WINDOW_HEIGHT - PADDING))
		self.display_surface = pygame.display.get_surface()

		# font
		self.font = pygame.font.Font(join('final-project','assets','NotoSans-Regular.ttf'), 30)

		# increment
		self.increment_height = self.surface.get_height() / 3

		# data 
		self.score = 0
		self.level = 1
		self.lines = 0

	def display_text(self, pos, text):
		text_surface = self.font.render(f'{text[0]}: {text[1]}', True, 'white')
		text_rext = text_surface.get_rect(center = pos)
		self.surface.blit(text_surface, text_rext)

	def run(self):

		self.surface.fill(GRAY)
		for i, text in enumerate([('Score',self.score), ('Level', self.level), ('Lines', self.lines)]):
			x = self.surface.get_width() / 2
			y = self.increment_height / 2 + i * self.increment_height
			self.display_text((x,y), text)

		self.display_surface.blit(self.surface,self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
