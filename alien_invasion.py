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
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)



    def _check_events(self):
            """respong to keypresses and mouse events"""    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_a:
                        self.ship.moving_left = True
                    

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_a:
                        self.ship.moving_left = False
                        


    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
            

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

