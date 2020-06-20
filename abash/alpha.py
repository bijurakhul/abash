from abash.utils.config import ConfigurationParser

class AlphaTerminal(ConfigurationParser):
  config_file = {}
  user_name = None

  def __init__(self):
    self.text("Initializing Alpha Bash Terminal")
    self.fetch_configuration_properties()

  def fetch_configuration_properties(self):
    self.config_file = self.read_from_config()
