import pygame


class Player():
    def __init__(self, screen):
        # Initialize player and set starting position
        self.screen = screen

        # Load image and get rect
        self.image = pygame.image.load("Images/Player.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starting position
        self.rect.centerx = self.screen_rect.centerx - 140
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # Draw the player on its current position
        self.screen.blit(self.image, self.rect)
