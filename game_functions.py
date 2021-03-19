import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien

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
    fire_bullet(ai_settings, screen, ship, bullets)

  elif event.key == pygame.K_q:
    sys.exit()

def check_keyup_events(event, ai_settings, screen, ship, bullets):
  """Responds to keypress"""
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  if event.key == pygame.K_LEFT:
      ship.moving_left = False



def update_screen(ai_settings, screen, ship, aliens, bullets):
  """Update the images on the screen and flip to a new screen"""
  screen.fill(ai_settings.bg_color)

  #redraw all bullets all bullets behind the ship and aliens
  for bullet in bullets.sprites():
    bullet.draw_bullet()

  # draw a ship on the screen
  ship.blitme()
  aliens.draw(screen)

  pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
  """Update the position of bullets and
  get rid of the old bullets that have left the screem"""

  bullets.update()
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)
  # check to see if any lasers have hit an alien craft
  # and if they have then destroy both objects

  check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
  """Fire a bullet if the bullet limit is not reached"""
  if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
  """create a full fleet of aliens"""
  alien = Alien(ai_settings, screen)
  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
  num_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

  # create the fleet of alien invaders
  for row in range(num_rows):
    for alien_number in range(number_aliens_x):
      create_alien(ai_settings, screen, aliens, alien_number, row)

def get_number_aliens_x(ai_settings, alien_width):
  """Determine the number of aliens that fit in a row"""
  available_space_x = ai_settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
  """Create an alien and place it in the row"""
  alien = Alien(ai_settings, screen)
  alien_width = alien.rect.width
  alien.x = alien_width + 2 * alien_width * alien_number
  alien.rect.x = alien.x
  alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
  aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
  """Determine the number of rows of aliens that can fit on the screen"""
  available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
  num_rows = int(available_space_y / (2 * alien_height))
  return num_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
  """Update the positions of the aliens"""
  check_fleet_edge(ai_settings, aliens)
  aliens.update()

  # look for alien/ship collisions
  if pygame.sprite.spritecollideany(ship, aliens):
    ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
  check_aliens_bottoms(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edge(ai_settings, aliens):
  """Respond appropriately when any aliens reach the edge of the screen"""
  for alien in aliens.sprites():
    if alien.check_edge():
      change_fleet_direction(ai_settings, aliens)
      break

def change_fleet_direction(ai_settings, aliens):
  """Change the direction of the alien fleets movements"""
  for alien in aliens.sprites():
    alien.rect.y += ai_settings.fleet_drop_speed
  ai_settings.fleet_direction *= -1

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
  """Respond to any bullet/alien collisions"""
  collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

  if len(aliens) == 0:
    # destroy existing lasers and create a new fleet
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
  """Responds to ship being hit by an alien"""
  if stats.ships_left > 0:
    stats.ships_left -= 1

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    sleep(.5)
  else:
    stats.game_active = False

def check_aliens_bottoms(ai_settings, stats, screen, ship, aliens, bullets):
  """Check to see if any aliens have reached the bottom of the screen"""
  screen_rect = screen.get_rect()
  for alien in aliens.sprites():
    if alien.rect.bottom >= screen_rect.bottom:
      ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
      break
