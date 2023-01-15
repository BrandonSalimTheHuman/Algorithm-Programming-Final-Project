import pygame


class Collision:
    def __init__(self, screen):
        # Initialize stuff
        self.counter = 0
        self.screen = screen
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font("font.ttf", 40)

        self.initialize_counter()

    def initialize_counter(self):
        # prepare image for text
        counter_string = str(self.counter)
        self.text1_image = self.font.render("Notes", True, self.text_color)
        self.text2_image = self.font.render("hit:", True, self.text_color)
        self.counter_image = self.font.render(counter_string, True, self.text_color)

        # get image rect
        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.counter_rect = self.counter_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # positioning rec
        self.text1_rect.right = self.screen_rect.right - 50
        self.text2_rect.centerx = self.text1_rect.centerx
        self.counter_rect.centerx = self.text1_rect.centerx

        self.text1_rect.top = 20
        self.text2_rect.top = 60
        self.counter_rect.top = 100

    def return_counter(self):
        return self.counter

    def update_counter(self, collision_counter):
        self.counter = collision_counter

    def draw_counter(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.counter_image, self.counter_rect)
