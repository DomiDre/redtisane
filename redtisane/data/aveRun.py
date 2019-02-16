import numpy as np
from .aveData import AveData
from ..utils import Logger
import glob

class AveragedRun():
  def __init__(self, folderPath, logger=None, *args):
    self.aveFiles = []
    self.aveData = []

    self.summedData = []

    # init the logger or use passed one
    self.log = Logger() if logger is None else logger

    if len(args) > 0 and ('[]' in folderPath):
      for addArgument in args:
        idx = folderPath.find('[]')
        self.folderPath = folderPath[:idx] + str(addArgument) + folderPath[idx+2:]
    else:
      self.folderPath = folderPath
    print(self.folderPath)
    self.load_folder()


  def load_folder(self):
    self.log.printLog(f'Loading folder: {self.folderPath}')
    self.aveFiles = sorted(glob.glob(self.folderPath))
    self.log.addShift()
    for i in range(len(self.aveFiles)):
      self.aveData.append(AveData(self.aveFiles[i], self.log))
    self.log.removeShift()

    self.nFiles = len(self.aveFiles)

  def sumAveData(self, sumEvery):
    assert self.nFiles % sumEvery == 0, f'The number of files in folder {self.folderPath} is not a multiple of the passed argument.'
    self.nSummedFiles = int(self.nFiles/sumEvery)
    self.sumEvery = sumEvery

    self.summedData = []
    for i in range(sumEvery):
      self.summedData.append(AveData())
      self.summedData[i].phi = self.aveData[i].phi
      for j in range(self.nSummedFiles):
        addData = self.aveData[i+j*sumEvery]
        self.summedData[i].I += addData.I
        self.summedData[i].sI += addData.sI**2
      self.summedData[i].sI = np.sqrt(self.summedData[i].sI)
