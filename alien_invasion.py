import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Inatilize the game, and create game rescources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)




    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watch for keyboard and mosue events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


            #make the most recently drawn scren visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

