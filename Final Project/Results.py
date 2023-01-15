import pygame


class Results:
    def __init__(self, note_count, collision_counter, screen):
        # Initialize stuff
        self.note_count = note_count
        self.collision_counter = collision_counter
        self.dodged_notes = note_count - collision_counter
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font1 = pygame.font.Font("font.ttf", 40)
        self.font2 = pygame.font.SysFont(None, 100)
        self.font3 = pygame.font.Font("font.ttf", 75)
        self.text_color1 = (0, 0, 0)
        self.text_color2 = (255, 0, 0)

        self.initialize_text()
        self.initialize_results()

    def initialize_text(self):
        # Prepare images
        self.line1_image = self.font3.render("RESULTS:", True, self.text_color1)
        self.line2_text = "Out of a total of " + str(self.note_count) + " notes,"
        self.line2_image = self.font1.render(self.line2_text, True, self.text_color1)
        self.line3_image = self.font1.render("you got hit:", True, self.text_color1)
        self.line4_image = self.font1.render("You dodged:", True, self.text_color1)
        self.line5_image = self.font1.render("of all the notes", True, self.text_color1)

        # Prepare rect
        self.line1_rect = self.line1_image.get_rect()
        self.line2_rect = self.line2_image.get_rect()
        self.line3_rect = self.line3_image.get_rect()
        self.line4_rect = self.line4_image.get_rect()
        self.line5_rect = self.line5_image.get_rect()

        # Positioning rect
        self.line1_rect.center = self.line2_rect.center = self.line3_rect.center = self.line4_rect.center = \
            self.line5_rect.center = self.screen_rect.center

        self.line1_rect.top = 100
        self.line2_rect.top = 250
        self.line3_rect.top = 300
        self.line4_rect.top = 500
        self.line5_rect.top = 700

    def initialize_results(self):
        # Create image for the number of collisions and the percentage
        self.collision_counter_image = self.font2.render(str(self.collision_counter) + " times", True, self.text_color2)
        self.percentage = f"{round((self.dodged_notes / self.note_count * 100), 1):g}"
        self.percentage_image = self.font2.render(str(self.percentage) + "%", True, self.text_color2)

        # Find rect
        self.collision_counter_rect = self.collision_counter_image.get_rect()
        self.percentage_rect = self.percentage_image.get_rect()

        # Positioning rect
        self.collision_counter_rect.center = self.percentage_rect.center = self.screen_rect.center

        self.collision_counter_rect.top = 400
        self.percentage_rect.top = 600
    
    def draw_results(self):
        self.screen.blit(self.line1_image, self.line1_rect)
        self.screen.blit(self.line2_image, self.line2_rect)
        self.screen.blit(self.line3_image, self.line3_rect)
        self.screen.blit(self.line4_image, self.line4_rect)
        self.screen.blit(self.line5_image, self.line5_rect)
        self.screen.blit(self.collision_counter_image, self.collision_counter_rect)
        self.screen.blit(self.percentage_image, self.percentage_rect)
