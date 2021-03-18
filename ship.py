import pygame

class Ship():
  """
  Class for the player's ship
  """
  def __init__(self, ai_settings, screen):
    """
    initialize the ship and set it's starting position
    """
    self.screen = screen
    self.ai_settings = ai_settings

    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # start each ship at the same place
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # store a decimal value for the ships center
    self.center = float(self.rect.centerx)

    # movement flag
    self.moving_right = False
    self.moving_left = False

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.ai_settings.ship_speed_factor
    elif self.moving_left and self.rect.left > 0:
      self.center -= self.ai_settings.ship_speed_factor
    # update the rect object
    self.rect.centerx = self.center
  
  def blitme(self):
    """
    draw the ship at it's current location
    """
    self.screen.blit(self.image, self.rect)