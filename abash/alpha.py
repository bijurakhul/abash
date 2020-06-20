from re import match
from abash.utils.config import ConfigurationParser

class AlphaTerminal(ConfigurationParser):
  config_file = {}
  user_name = None

  def __init__(self):
    self.text("Initializing Alpha Bash Terminal")
    self.fetch_configuration_properties()
    self.fetch_user_details()

  # Fetch the configuration file data to use in the application
  def fetch_configuration_properties(self):
    self.config_file = self.read_from_config()

  # Fetch the user name from configuration data or create the user
  def fetch_user_details(self):
    self.user_name = self.get_config_value("userName")

    if self.user_name:
      self.text("User name fetched successfully")
    else:
      self.text("No user found", self.FAILUREMSG)

      # Get Username and check if the user has entered correctly and write to comfiguration file
      self.user_name = input("Enter a user name: ")
      if match("^[A-Za-z0-9]*$", self.user_name):
        self.config_file["userName"] = self.user_name
        self.text("Username updated successfully")
        self.write_to_config()
        return
      else:
        self.text("Username must contain only alphabets and numerals", self.WARNINGMSG)
        self.user_name = None
        self.fetch_user_details()

    return
