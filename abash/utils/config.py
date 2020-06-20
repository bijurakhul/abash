import json
from os.path import exists
from abash.utils.fileio import FileHandler

CONFIGURATION_FILE = "config.json"

class ConfigurationParser(FileHandler):

  # Checks if the configuration file exists
  def check_for_config_file(self):
    if exists(f"./abash/{CONFIGURATION_FILE}"):
      return True
    else:
      self.text("Configuration file doesn't exist", self.FAILUREMSG)
      exit()

  # Reads the config file and stores it in a varaible as a dictionary
  def read_from_config(self):
    self.text("Fetching Configuration file")
    self.check_for_config_file()
    return json.loads(self.read_from_file(f"./abash/{CONFIGURATION_FILE}"))

  # Write the configuration file data to the file from memory
  def write_to_config(self):
    self.text("Writing Configuration information to file")
    self.check_for_config_file()
    self.write_to_file(json.dumps(self.config_file), f"./abash/{CONFIGURATION_FILE}")

  # Get the value of the specified property
  def get_config_value(self, property):
    if bool(self.config_file):
      return self.config_file[property] if property in self.config_file else None
    return None

  # Set the value of the property in the configuration object in memory
  def set_config_value(self, property, value):
    if bool(self.config_file):
      self.config_file[property] = value
