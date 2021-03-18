class Settings():
  """
  A class to store all of the settings
  for my alien adventure game
  """
  
  def __init__(self):
    """
    initaliaze the game's settings
    """
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230,230,230)

    # ship settings
    self.ship_speed_factor = 1.5

    # bullet settings
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = 66, 33, 99
    self.bullets_allowed = 4