import pygame
from pygame.sprite import Sprite

from dino_runner.components import game
from dino_runner.utils.constants import HEART


class Heaths(Sprite):

    def __init__(self):
        self.heaths = [HEART, HEART, HEART]
        self.image = HEART
        self.heath_rect = self.image.get_rect()
        self.heath_rect.x = 20
        self.heath_rect.y = 30

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.heath_rect.x, self.heath_rect.y))
        screen.blit(self.image, (self.heath_rect.x + 30, self.heath_rect.y))
        screen.blit(self.image, (self.heath_rect.x + 60, self.heath_rect.y))



