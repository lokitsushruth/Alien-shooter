import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.scale_factor = 2
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_factor), int(self.image.get_height() * self.scale_factor)))

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x