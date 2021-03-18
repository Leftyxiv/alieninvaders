import pygame

class Ship():
  """
  Class for the player's ship
  """
  def __init__(self, screen):
    """
    initialize the ship and set it's starting position
    """
    self.screen = screen

    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # start each ship at the same place
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    # movement flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    if self.moving_right:
      self.rect.centerx += 1
    elif self.moving_left:
      self.rect.centerx -= 1
  
  def blitme(self):
    """
    draw the ship at it's current location
    """
    self.screen.blit(self.image, self.rect)