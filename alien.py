import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent an alien peon among the fleet"""

  def __init__(self, ai_settings, screen):
    """Initialize a new alien and set it's position"""
    super(Alien, self).__init__()
    self.screen = screen
    self.ai_settings = ai_settings
    
    # load the alien image and set its attribute
    self.image = pygame.image.load('images/alien.bmp')
    self.rect = self.image.get_rect()

    # give alien coords
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # stpre position
    self.x = float(self.rect.x)

  def blitme(self):
    """Draw the alien on the screen"""
    self.screen.blit(self.image, self.rect)

  def update(self):
    """Move the alien ships to the right"""
    self.x += self.ai_settings.alien_speed_factor
    self.rect.x = self.x