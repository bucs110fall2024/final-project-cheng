# src/preview.py
import pygame
import os
from pygame.image import load
from os.path import join
from .tetrominos import TETROMINOS

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


class Preview:
	def __init__(self):
		
		# general
		self.display_surface = pygame.display.get_surface()
		self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT))
		self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING,PADDING))

		# shapes
		self.shape_surfaces = {shape: load(join('final-project','assets',f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys()}

		# image position data
		self.increment_height = self.surface.get_height() / 3

	def display_pieces(self, shapes):
		for i, shape in enumerate(shapes):
			shape_surface = self.shape_surfaces[shape]
			x = self.surface.get_width() / 2
			y = self.increment_height / 2 + i * self.increment_height
			rect = shape_surface.get_rect(center = (x,y))
			self.surface.blit(shape_surface,rect)

	def run(self, next_shapes):
		self.surface.fill(GRAY)
		self.display_pieces(next_shapes)
		self.display_surface.blit(self.surface, self.rect)
		pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
