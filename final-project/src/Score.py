import pygame
from os.path import join
from .settings import *

class Score:
	def __init__(self):
		self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT - PADDING))
		self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING,WINDOW_HEIGHT - PADDING))
		self.display_surface = pygame.display.get_surface()

		# font
		self.font = pygame.font.Font(join('final-project','assets','font','NotoSans-Regular.ttf'), 30)

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
