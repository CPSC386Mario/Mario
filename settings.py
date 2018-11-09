class Settings:
    """A class to store all settings for Pacman"""

    def __init__(self):
        """Initializes the game's static settings"""

        self.screen_width = 1000
        self.screen_height = 680
        # Sets background color
        self.bg_color = (0, 0, 0)

        # Mario settings
        self.mario_limit = 3
        self.base_level = self.screen_height - 80
