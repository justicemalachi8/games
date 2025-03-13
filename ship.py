import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initalize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a float for the ships exact horizontal position.
        self.x = float(self.rect.x)

        #movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag."""
        #update the ship's x value, not the rect
        if self.moving_right:
            self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= 1
            self.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current loccation."""
        self.screen.blit(self.image, self.rect)