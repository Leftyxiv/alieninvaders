import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """A class to manage the lasers the ship shoots"""
  
  def __init__(self, ai_settings, screen, ship):
    """Create a bullet object at the ship's current position"""
    # can also just call super().__init__()
    super(Bullet, self).__init__()
    self.screen = screen

    # create a bullet rect at 0,0 and then set to current position 
    self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top

    # store the bullets position
    self.y = float(self.rect.top)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor


  def update(self):
    """Move the bullet across the screen"""
    self.y -= self.speed_factor
    self.rect.y = self.y

  def draw_bullet(self):
    """Draw the bullet on the screen"""
    pygame.draw.rect(self.screen, self.color, self.rect)