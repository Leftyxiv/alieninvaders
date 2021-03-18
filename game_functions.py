import sys

import pygame

def check_events(ship):
  """Respond to keypresses and mouse events"""
  def check_keydown_events(event, ship):
    """Responds to keypress"""
    if event.key == pygame.K_RIGHT:
      # move ship to the right
      ship.moving_right = True

    elif event.key == pygame.K_LEFT:
      # move ship to the right
      ship.moving_left = True

  def check_keyup_events(event, ship):
    """Responds to keypress"""
    if event.key == pygame.K_RIGHT:
      ship.moving_right = False
          
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ship)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
  """Update the images on the screen and flip to a new screen"""
  screen.fill(ai_settings.bg_color)
  # draw a ship on the screen
  ship.blitme()

  pygame.display.flip()
