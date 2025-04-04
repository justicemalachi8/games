import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Inatilize the game, and create game rescources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

            



    def _check_events(self):
            """respong to keypresses and mouse events"""    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):
        """respond to keypresses."""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                    

                
    def _check_keyup_events(self,event):
        """respond to key releases"""  
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False   

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_sllowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  

    def _update_bullets(self):
        """update the position of bullets andget rif og old bullets"""
        # update bullet positons       
        self.bullets.update()

        #get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)        



    def _create_fleet(self):
        """Create the fleet of aliens."""
        #create an elien and keep adding aliens till theres no room left
        #spacing between aliens is one alien width
        
        alien = Alien(self)
        alien_width = alien.rect.width
        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            
            self._create_alien(current_x)
            current_x += 2 * alien_width
    def _create_alien(self, x_position):
            
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)
            

    
    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
            

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

