from abash.utils.display import DisplayText

class FileHandler(DisplayText):
  file_handler = None
  file_data = None

  # Open a file and return the file handler
  def __open_file(self, file_name, file_open_mode):
    try:
      self.file_handler = open(file_name, file_open_mode)
    except FileNotFoundError:
      self.text(f"Unable to open file {file_name}")

  # Open and read data from the given file
  def read_from_file(self, file_name):
    self.__open_file(file_name, "r")
    if self.file_handler:
      try:
        self.file_data = self.file_handler.read()
        self.file_handler.close()
      except IOError:
        self.text(f"Unexpedcted Error while reading {file_name}", self.FAILUREMSG)
        exit()
    return self.file_data

  # Open a file and write data to the file
  def write_to_file(self, file_data, file_name, file_write_mode = "w"):
    self.__open_file(file_name, file_write_mode)
    if self.file_handler:
      try:
        self.file_handler.write(file_data)
        self.file_handler.close()
      except IOError:
        self.text(f"Unexpedcted Error while writing to {file_name}", self.FAILUREMSG)
        exit()
    return
