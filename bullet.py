import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        """create a bullet object at the ship's position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) then set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # store bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up"""
        # update the bullet position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
