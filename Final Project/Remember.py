import pygame


class RememberThisPattern:
    def __init__(self, screen):
        # Initialize stuff
        self.screen = screen
        self.text_color = (0, 0, 139)
        self.font = pygame.font.Font("font2.ttf", 40)

        self.initialize_text1()

    def initialize_text1(self):
        # Create images for text
        self.line1_image = self.font.render("Remember", True, self.text_color)
        self.line2_image = self.font.render("this", True, self.text_color)
        self.line3_image = self.font.render("pattern!", True, self.text_color)

        # Find rect
        self.line1_rect = self.line1_image.get_rect()
        self.line2_rect = self.line2_image.get_rect()
        self.line3_rect = self.line3_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Positioning rect
        self.line1_rect.right = self.screen_rect.right - 10
        self.line2_rect.centerx = self.line1_rect.centerx
        self.line3_rect.centerx = self.line1_rect.centerx

        self.line1_rect.top = 400
        self.line2_rect.top = 460
        self.line3_rect.top = 520
    
    def initialize_text2(self):
        # Create images for second set of text
        self.line4_image = self.font.render("Keep", True, self.text_color)
        self.line5_image = self.font.render("the", True, self.text_color)
        self.line6_image = self.font.render("pattern,", True, self.text_color)
        self.line7_image = self.font.render("no", True, self.text_color)
        self.line8_image = self.font.render("matter", True, self.text_color)
        self.line9_image = self.font.render("what!", True, self.text_color)

        # Find rect
        self.line4_rect = self.line4_image.get_rect()
        self.line5_rect = self.line5_image.get_rect()
        self.line6_rect = self.line6_image.get_rect()
        self.line7_rect = self.line7_image.get_rect()
        self.line8_rect = self.line8_image.get_rect()
        self.line9_rect = self.line9_image.get_rect()

        # Positioning images
        self.line4_rect.centerx = self.line5_rect.centerx = self.line6_rect.centerx = self.line7_rect.centerx = \
            self.line8_rect.centerx = self.line9_rect.centerx = self.line1_rect.centerx

        self.line4_rect.top = 300
        self.line5_rect.top = 360
        self.line6_rect.top = 420
        self.line7_rect.top = 560
        self.line8_rect.top = 620
        self.line9_rect.top = 680

    def draw_text(self):
        # Draw first set of text
        self.screen.blit(self.line1_image, self.line1_rect)
        self.screen.blit(self.line2_image, self.line2_rect)
        self.screen.blit(self.line3_image, self.line3_rect)

    def draw_text2(self):
        # Draw second set of text
        self.screen.blit(self.line4_image, self.line4_rect)
        self.screen.blit(self.line5_image, self.line5_rect)
        self.screen.blit(self.line6_image, self.line6_rect)
        self.screen.blit(self.line7_image, self.line7_rect)
        self.screen.blit(self.line8_image, self.line8_rect)
        self.screen.blit(self.line9_image, self.line9_rect)
