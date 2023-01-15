import pygame


class Rules:
    def __init__(self, screen):
        # Initialize stuff
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (112, 41, 99)
        self.text_color2 = (0, 0, 0)
        self.font = pygame.font.Font("font.ttf", 30)
        self.font2 = pygame.font.Font("font4.ttf", 75)

        self.initialize_rules()

    def initialize_rules(self):
        # Create image for text
        self.text1_image = self.font.render("Your goal is to", True, self.text_color)
        self.text2_image = self.font2.render("DODGE THE NOTES", True, self.text_color2)
        self.text3_image = self.font.render("To switch between lanes,", True, self.text_color)
        self.text4_image = self.font.render("use the left and right arrow keys", True, self.text_color)
        self.text5_image = self.font.render("or use the 'a' and 'd' keys.", True, self.text_color)
        self.text6_image = self.font.render("If you are at the rightmost lane and go right,", True, self.text_color)
        self.text7_image = self.font.render("you will end up at the leftmost lane.", True, self.text_color)
        self.text8_image = self.font.render("If you are at the leftmost lane and go left,",
                                            True, self.text_color)
        self.text9_image = self.font.render("you will end up at the rightmost lane.", True, self.text_color)
        self.text10_image = self.font.render("Press enter again to start the game!", True, self.text_color)

        # Find rect
        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.text5_rect = self.text5_image.get_rect()
        self.text6_rect = self.text6_image.get_rect()
        self.text7_rect = self.text7_image.get_rect()
        self.text8_rect = self.text8_image.get_rect()
        self.text9_rect = self.text9_image.get_rect()
        self.text10_rect = self.text10_image.get_rect()

        # Positioning images
        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.text5_rect.center = self.text6_rect.center = self.text7_rect.center = self.text8_rect.center = \
            self.text9_rect.center = self.text10_rect.center = self.screen_rect.center

        self.text1_rect.centery -= 400
        self.text2_rect.centery -= 300
        self.text3_rect.centery -= 100
        self.text4_rect.centery -= 50
        self.text5_rect.centery -= 0
        self.text6_rect.centery += 100
        self.text7_rect.centery += 150
        self.text8_rect.centery += 200
        self.text9_rect.centery += 250
        self.text10_rect.centery += 400

    def draw_rules(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        self.screen.blit(self.text4_image, self.text4_rect)
        self.screen.blit(self.text5_image, self.text5_rect)
        self.screen.blit(self.text6_image, self.text6_rect)
        self.screen.blit(self.text7_image, self.text7_rect)
        self.screen.blit(self.text8_image, self.text8_rect)
        self.screen.blit(self.text9_image, self.text9_rect)
        self.screen.blit(self.text10_image, self.text10_rect)