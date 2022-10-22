import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        """intialize alien and its starting position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # load alien image
        self.image = pygame.image.load("images/alien.png")
        #self.scaled_image = pygame.transform.scale(self.image, (10, 16))
        self.rect = self.image.get_rect()

        # start each new alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """move alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """return true if alien is at the screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
