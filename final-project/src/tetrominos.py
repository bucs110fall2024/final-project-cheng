from .settings import *

class Tetromino:
	def __init__(self, shape, group, create_new_tetromino, field_data):
		"""
	Initializes a Tetromino instance with its shape, group, and position data.

    Args:
        shape (str): The type of Tetromino (e.g., 'I', 'O', 'T', etc.).
        group (object): The group to which the Tetromino's blocks belong.
        create_new_tetromino (function): A function to create a new Tetromino when the current one is placed.
        field_data (list): A 2D list representing the game field's current state.

    Returns:
        None
	"""
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
		"""
    Checks if the Tetromino will collide with another object when moving horizontally.

    Args:
        blocks (list): A list of Block objects representing the Tetromino.
        amount (int): The number of units to move horizontally.

    Returns:
        bool: True if a collision is detected; otherwise, False.
    """
		collision_list = [block.horizontal_collide(int(block.pos.x + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	def next_move_vertical_collide(self, blocks, amount):
		"""
    Checks if the Tetromino will collide with another object when moving vertically.

    Args:
        blocks (list): A list of Block objects representing the Tetromino.
        amount (int): The number of units to move vertically.

    Returns:
        bool: True if a collision is detected; otherwise, False.
    """
		collision_list = [block.vertical_collide(int(block.pos.y + amount), self.field_data) for block in self.blocks]
		return True if any(collision_list) else False

	# movement
	def move_horizontal(self, amount): 
		"""
    Moves the Tetromino horizontally if no collision is detected.

    Args:
        amount (int): The number of units to move horizontally.

    Returns:
		None
       """
		if not self.next_move_horizontal_collide(self.blocks, amount):
			for block in self.blocks:
				block.pos.x += amount

	def move_down(self):
		"""
    Moves the Tetromino down one unit if no collision is detected. If a collision occurs,
    it places the Tetromino on the field and creates a new Tetromino.

    Args:
        None

    Returns:
        None
    """
		if not self.next_move_vertical_collide(self.blocks, 1):
			for block in self.blocks:
				block.pos.y += 1
		else:
			for block in self.blocks:
				self.field_data[int(block.pos.y)][int(block.pos.x)] = block
			self.create_new_tetromino()
	# drop
	def instant_drop(self):
		"""
    Instantly drops the Tetromino to the lowest valid position and places it on the field.

    Args:
        None

    Returns:
        None
    """
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
			print(f"Game Over {e}")

	# rotate
	def rotate(self):
		"""
    Rotates the Tetromino around its pivot point, if no collision is detected.

    Args:
        None

    Returns:
        None
    """
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
		"""
    Initializes a Block instance with its group, position, and color.

    Args:
        group (object): The group to which the block belongs.
        pos (tuple): The initial position of the block as (x, y).
        color (tuple): The RGB color of the block.

    Returns:
        None
    """
		# general
		super().__init__(group)
		self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
		self.image.fill(color)
		
		# position
		self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
		self.rect = self.image.get_rect(topleft = self.pos * BLOCK_SIZE)

	def rotate(self, pivot_pos):
		"""
    Rotates the block around a pivot point.

    Args:
        pivot_pos (pygame.Vector2): The pivot position around which the block will rotate.

    Returns:
        pygame.Vector2: The new position of the block after rotation.
    """
		return pivot_pos + (self.pos - pivot_pos).rotate(90)

	def horizontal_collide(self, x, field_data):
		"""
    Checks if the block will collide horizontally with the game field's boundaries or another block.

    Args:
        x (int): The x-coordinate to check for collision.
        field_data (list): A 2D list representing the game field's current state.

    Returns:
        bool: True if a collision is detected; otherwise, False.
    """
		if not 0 <= x < COLUMNS:
			return True
		if field_data[int(self.pos.y)][x]:
			return True

	def vertical_collide(self, y, field_data):
		"""
    Checks if the block will collide vertically with the game field's boundaries or another block.

    Args:
        y (int): The y-coordinate to check for collision.
        field_data (list): A 2D list representing the game field's current state.

    Returns:
        bool: True if a collision is detected; otherwise, False.
    """
		if y >= ROWS:
			return True
		if y >= 0 and field_data[y][int(self.pos.x)]:
			return True

	def update(self):
		"""
    Updates the block's position on the screen based on its current logical position.

    Args:
        None

    Returns:
        None
    """
		self.rect.topleft = self.pos * BLOCK_SIZE
