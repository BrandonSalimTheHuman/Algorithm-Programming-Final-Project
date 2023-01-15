class Settings:
    # Class to store all settings

    def __init__(self):
        # Screen settings
        self.screen_width = 820
        self.screen_height = 900

        # background color
        self.bg_color = (204, 204, 255)

        # Offset. Change this if the game doesn't sync
        self.offset = 900

        # Game state settings. Starts at the title screen
        self.game_state = "Start"

        # Song select
        self.song = ""
