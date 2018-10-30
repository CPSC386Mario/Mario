class Settings:
    """A class to store all settings for Pacman"""

    def __init__(self):
        """Initializes the game's static settings"""

        self.screen_width = 800
        self.screen_height = 600
        # Sets background color
        self.bg_color = (0, 255, 255)

        # Ship settings
        self.mario_limit = 3
