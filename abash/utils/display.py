class DisplayText:
  SUCCESSMSG = "\033[32m"
  FAILUREMSG = "\033[31m"
  WARNINGMSG = "\033[33m"
  RESETCOLOR = "\033[37m"

  def text(self, msg, status_color = SUCCESSMSG):
    status_symbol = "+" if status_color == self.SUCCESSMSG else "-"
    text_reset = self.RESETCOLOR

    print(f"{status_color}[{status_symbol}]{text_reset} {msg}")
