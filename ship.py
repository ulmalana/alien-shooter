import pygame

class Ship:
    def __init__(self, game):
        """Initialize the ship and the starting position"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # load the ship image
        self.image = pygame.image.load("images/ship.png")
        #self.scaled_image = pygame.transform.scale(self.image, (40, 70))
        self.rect = self.image.get_rect()

        # put the ship at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False
        self.moving_left = False

        # store decimal value of the ship's horizontal position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the ship at its location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update ship's position based on movement flag"""

        # move the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
