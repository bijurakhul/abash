import json
import os
from abash.utils.fileio import FileHandling

CONFIGURATION_FILE = "config.json"

config_file_handler = None
user_name = None
config_file = {}

class AlphaTerminal(FileHandling):
  def __init__(self):
    self.text("Initializing Alpha Bash Terminal")
    self.check_existing_user()

  # Create a new user 
  def create_new_user(self):
    global config_file_handler, user_name

    self.text("Creating new user")
    user_name = input("Enter the user name: ")
    config_file["user"] = user_name

    self.write_to_file(json.dumps(config_file), CONFIGURATION_FILE)
    self.text("User created successfully")
  
  # Check if existing user is found in the config file
  def check_existing_user(self):
    global config_file, user_name

    self.text("Searching for Configuration file")

    if os.path.exists("config.json"):
      self.text("Fetching user from Configuration file")
      config_file = json.loads(self.read_from_file(CONFIGURATION_FILE))
      user_name = config_file["user"]
    else:
      self.text("Configuration file not found", self.FAILUREMSG)
      self.create_new_user()
