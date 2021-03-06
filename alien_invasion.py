import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats

import game_functions as gf

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption('Alien Invasion')

  # bg_color = (230, 230, 230)
  # create a ship
  stats = GameStats(ai_settings)
  ship = Ship(ai_settings, screen)
  # alien = Alien(ai_settings, screen)
  bullets = Group()
  aliens = Group()

  # create a fleet of aliens
  gf.create_fleet(ai_settings, screen, ship, aliens)

  while True:
    gf.check_events(ai_settings, screen, ship, bullets)

    if stats.game_active:
      ship.update()
      # bullets.update()
      gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
      gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
      gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()