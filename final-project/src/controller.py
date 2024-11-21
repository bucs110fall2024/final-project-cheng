from settings import *
from Game import Game
from Score import Score
from Preview import Preview

class Controller:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris Game")
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.score = Score()
        self.preview = Preview()



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.blit(self.surface, self.rect)
            self.display_surface.fill(GRAY)

            self.game.run()
            self.score.run()
            self.preview.run()

            pygame.display.update()
            self.clock.tick(60)