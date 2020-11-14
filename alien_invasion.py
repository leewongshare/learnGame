import sys

import pygame

from settings import Settings

class AlienInvasion:

    def __init__(self):
        
        pygame.init()

        self.settings = Settings()
    
        #self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode(
                        (self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):

        self.screen.fill(self.settings.bg_color)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                       sys.exit()

        pygame.display.flip()
        
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

