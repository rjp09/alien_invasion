import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represents a single alien in the fleet. """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if an alien is at the edge of the screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left. """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x