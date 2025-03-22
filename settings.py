
class Settings:
    """a class to store all settings for alien invasion."""

    def __init__(self):
        """initalize the game's settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        #SHIP SETTINGS
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_sllowed = 3