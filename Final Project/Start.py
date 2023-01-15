import pygame


class Start:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)
        self.text_color2 = (240, 235, 255)
        self.font = pygame.font.Font("font3.ttf", 50)
        self.font2 = pygame.font.Font("font.ttf", 20)
        self.font3 = pygame.font.Font("font3.ttf", 35)

        self.song = ""
        self.bpm = ""

    def initialize_start_text(self):
        self.text1_image = self.font.render("PRESS ENTER TO", True, self.text_color)
        self.text2_image = self.font.render("START THE GAME", True, self.text_color)
        self.text3_image = self.font2.render("OR PRESS SPACE TO VIEW RULES", True, self.text_color)
        self.text4_image = self.font3.render(self.song, True, self.text_color2)
        self.text5_image = self.font2.render("By Riya", True, self.text_color2)
        self.text6_image = self.font2.render("BPM: " + self.bpm, True, self.text_color2)
        self.background = pygame.Rect(0, 0, 300, 175)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.text5_rect = self.text5_image.get_rect()
        self.text6_rect = self.text6_image.get_rect()

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.text5_rect.center = self.text6_rect.center = self.background.center = self.screen_rect.center

        self.text1_rect.centery -= 100
        self.text3_rect.centery += 100
        self.text5_rect.centery += 50
        self.text6_rect.centery += 100
        self.background.centery += 50
        self.text4_rect.centerx = self.text5_rect.centerx = self.text6_rect.centerx = self.background.centerx = \
            self.screen_rect.centerx - 75

    def draw_start(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)

    def draw_intro(self):
        self.screen.fill((100, 17, 151), self.background)
        self.screen.blit(self.text4_image, self.text4_rect)
        self.screen.blit(self.text5_image, self.text5_rect)
        self.screen.blit(self.text6_image, self.text6_rect)

    def update_song_and_bpm(self, song, bpm):
        self.song = song
        self.bpm = bpm
        self.initialize_start_text()
