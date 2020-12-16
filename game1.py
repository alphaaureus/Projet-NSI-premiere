# Test
import pygame

# Infos pour le jeu sa police et les couleurs
class Game():
    def _init_(self):
        pygame.init()
        self.running, self.playing= True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1080,720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window - pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)

# Infos pour le jeu sa police et les couleurs
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

# Verifie si le joueur joue ou veut quitter
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

# Attribue au cle le bool False
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
