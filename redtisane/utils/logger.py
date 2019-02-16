import numpy as np

class Logger:
  def __init__(self):
    # Init variables
    self.log = ""
    self.shift = ""
  def printLog(self, message):
    self.log += self.shift + '#' + message + '\n'
    print(self.shift + message)

  def addShift(self):
    self.shift = self.shift + '\t'

  def removeShift(self):
    self.shift = self.shift.rsplit('\t', 1)[0]
