from pygame.time import get_ticks

class Timer:
	def __init__(self, duration, repeated = False, func = None):
		"""
    Initializes a timer with a specified duration, repeat behavior, and optional callback function.

    Args:
        duration (int): The duration of the timer in milliseconds.
        repeated (bool, optional): Whether the timer should restart automatically after completion. Defaults to False.
        func (callable, optional): A function to execute when the timer completes. Defaults to None.

    Returns:
        None
    """
		self.repeated = repeated
		self.func = func
		self.duration = duration

		self.start_time = 0
		self.active = False

	def activate(self):
		"""
    Activates the timer and records the current start time.

    Args:
        None

    Returns:
        None
    """
		self.active = True
		self.start_time = get_ticks()

	def deactivate(self):
		"""
    Deactivates the timer and resets the start time.

    Args:
        None

    Returns:
        None
    """
		self.active = False
		self.start_time = 0

	def update(self):
		"""
    Checks if the timer has reached its duration. If so, executes the optional callback function, 
    deactivates the timer, and optionally reactivates it if it is set to repeat.

    Args:
        None

    Returns:
        None
    """
		current_time = get_ticks()
		if current_time - self.start_time >= self.duration and self.active:
			
			if self.func and self.start_time != 0:
				self.func()

			# reset timer
			self.deactivate()

			# repeat the timer
			if self.repeated:
				self.activate()