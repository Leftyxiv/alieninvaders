import sys

import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
  """Respond to keypresses and mouse events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, screen, ship, bullets)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ai_settings, screen, ship, bullets)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
  """Responds to keypress"""
  if event.key == pygame.K_RIGHT:
    # move ship to the right
    ship.moving_right = True

  elif event.key == pygame.K_LEFT:
    # move ship to the right
    ship.moving_left = True

  elif event.key == pygame.K_SPACE:
    if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)

def check_keyup_events(event, ai_settings, screen, ship, bullets):
  """Responds to keypress"""
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  if event.key == pygame.K_LEFT:
      ship.moving_left = False



def update_screen(ai_settings, screen, ship, bullets):
  """Update the images on the screen and flip to a new screen"""
  screen.fill(ai_settings.bg_color)

  #redraw all bullets all bullets behind the ship and aliens
  for bullet in bullets.sprites():
    bullet.draw_bullet()

  # draw a ship on the screen
  ship.blitme()

  pygame.display.flip()

def update_bullets(bullets):
  """Update the position of bullets and
  get rid of the old bullets that have left the screem"""

  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)