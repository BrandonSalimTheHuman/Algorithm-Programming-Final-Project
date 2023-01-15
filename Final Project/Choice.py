import pygame


class Choice:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.Font("font.ttf", 80)
        self.font2 = pygame.font.Font("font.ttf", 45)
        self.font3 = pygame.font.Font("font2.ttf", 25)
        self.text_color = (0, 0, 0)
        self.text_color2 = (255, 0, 150)

        self.prepare_text()

    def prepare_text(self):
        # Prepare images
        self.line1_image = self.font.render("Choose a song:", True, self.text_color2)
        self.line2_image = self.font2.render("Press 1 to choose Final Hope", True, self.text_color)
        self.line3_image = self.font3.render("Normal charting, but with gimmicks.", True, self.text_color)
        self.line4_image = self.font2.render("Press 2 to choose Cleyera", True, self.text_color)
        self.line5_image = self.font3.render("No gimmicks, but significantly harder charting.", True, self.text_color)

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
        self.line2_rect.top = 300
        self.line3_rect.top = 450
        self.line4_rect.top = 550
        self.line5_rect.top = 700

    def draw_text(self):
        self.screen.blit(self.line1_image, self.line1_rect)
        self.screen.blit(self.line2_image, self.line2_rect)
        self.screen.blit(self.line3_image, self.line3_rect)
        self.screen.blit(self.line4_image, self.line4_rect)
        self.screen.blit(self.line5_image, self.line5_rect)
