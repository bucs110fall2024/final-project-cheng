import pygame

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

class Tetromino:
	def __init__(self, shape, group, create_new_tetromino, field_data):

		# setup 
		self.shape = shape
		self.block_positions = TETROMINOS[shape]['shape']
		self.color = TETROMINOS[shape]['color']
		self.create_new_tetromino = create_new_tetromino
		self.field_data = field_data

		# create blocks
		self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]
	

	# collisions
	def next_move_horizontal_collide(self, blocks, amount):
		collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	def next_move_vertical_collide(self, blocks, amount):
		collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	# movement
	def move_horizontal(self, amount):
		if not self.next_move_horizontal_collide(self.blocks, amount):
			for block in self.blocks:
				block.pos.x += amount

	def move_down(self):
		if not self.next_move_vertical_collide(self.blocks, 1):
			for block in self.blocks:
				block.pos.y += 1
		else:
			for block in self.blocks:
				self.field_data[int(block.pos.y)][int(block.pos.x)] = block
			self.create_new_tetromino()
	# drop
	def instant_drop(self):
		"""Instantly drop the Tetromino to the lowest valid position."""
		try:
			# Drop the Tetromino as far down as possible
			while not self.next_move_vertical_collide(self.blocks, 1):
				for block in self.blocks:
					block.pos.y += 1
        	
			# Place the Tetromino on the field
			for block in self.blocks:
				x, y = int(block.pos.x), int(block.pos.y)
				if 0 <= y < ROWS:  # Ensure the block is within bounds
					if self.field_data[y][x] == 0:  # Ensure no duplicate placement
						self.field_data[y][x] = block
				else:
					raise ValueError()

		# Safely create the new Tetromino
			if not self.next_move_vertical_collide(self.blocks, 1):  # Avoid redundant creation
				self.create_new_tetromino()

		except Exception as e:
			# Log the issue for debugging
			print(f"Error during instant drop: {e}")

	# rotate
	def rotate(self):
		if self.shape != 'O':

			# 1. pivot point 
			pivot_pos = self.blocks[0].pos

			# 2. new block positions
			new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

			# 3. collision check
			for pos in new_block_positions:
				# horizontal 
				if pos.x < 0 or pos.x >= COLUMNS:
					return

				# field check -> collision with other pieces
				if self.field_data[int(pos.y)][int(pos.x)]:
					return

				# vertical / floor check
				if pos.y > ROWS:
					return

			# 4. implement new positions
			for i, block in enumerate(self.blocks):
				block.pos = new_block_positions[i]
	

class Block(pygame.sprite.Sprite):
	def __init__(self, group, pos, color):
		
		# general
		super().__init__(group)
		self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
		self.image.fill(color)
		
		# position
		self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
		self.rect = self.image.get_rect(topleft = self.pos * BLOCK_SIZE)

	def rotate(self, pivot_pos):

		return pivot_pos + (self.pos - pivot_pos).rotate(90)

	def horizontal_collide(self, x, field_data):
		if not 0 <= x < COLUMNS:
			return True

		if field_data[int(self.pos.y)][x]:
			return True

	def vertical_collide(self, y, field_data):
		if y >= ROWS:
			return True

		if y >= 0 and field_data[y][int(self.pos.x)]:
			return True

	def update(self):

		self.rect.topleft = self.pos * BLOCK_SIZE
