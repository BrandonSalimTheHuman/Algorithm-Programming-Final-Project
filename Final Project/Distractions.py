import pygame


class Distractions:
    def __init__(self, screen):
        # Initialize stuff
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.initialize_image()
        self.initialize_rect()

    def initialize_image(self):
        # Prepare THE HAND
        self.image = pygame.image.load("Images/THE HAND.png")
        self.image = pygame.transform.scale(self.image, (850, 575))

        # Find and position rect
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = 250
        self.image_rect.centery = -288

    def initialize_rect(self):
        # Rect has the same color as the background to hide the player
        self.rect = pygame.Rect(0, 0, 75, 75)
        self.color = (204, 204, 255)

    def return_image_centery(self):
        return self.image_rect.centery

    def update_image_centery(self, y_value):
        self.image_rect.centery = y_value

    def update_rect_center(self, center):
        self.rect.center = center

    def draw_image(self):
        self.screen.blit(self.image, self.image_rect)

    def draw_rect(self):
        self.screen.fill(self.color, self.rect)
