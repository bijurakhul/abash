class DisplayText:
  SUCCESSMSG = 0
  FAILUREMSG = 1

  text_colors = {
    "TGREEN": "\033[32m",
    "TWHITE": "\033[37m",
    "TRED": "\033[31m" 
  }

  def text(self, msg, status = SUCCESSMSG):
    status_color = self.text_colors["TGREEN"] if status == self.SUCCESSMSG else self.text_colors["TRED"]
    status_symbol = "+" if status == self.SUCCESSMSG else "-"
    text_reset = self.text_colors["TWHITE"]

    print(f"{status_color}[{status_symbol}]{text_reset} {msg}")
