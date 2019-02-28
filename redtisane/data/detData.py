from .RAWFile import RAWFile
from ..utils import Logger
import numpy as np

class DetData:
  def __init__(self, rawfile=None, logger=None):
    # Init variables
    self.log = Logger() if logger is None else logger
    self.y  = 0
    self.z  = 0
    self.I    = 0
    self.sI   = 0
    # self.parameters = {}

    if rawfile is not None:
      # Load file
      self.load_file(rawfile)

  def load_file(self, datafile):
    rawFile = RAWFile(datafile)
    rawFile.readFile()
    rawFile.readHeader()
    rawFile.readDetector()
    self.I = rawFile['rawCounts']
    self.sI = np.sqrt(self.I)
    Ny, Nz = self.I.shape
    self.y = np.arange(Ny)
    self.z = np.arange(Nz)