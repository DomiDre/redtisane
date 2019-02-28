import numpy as np
from .detData import DetData
from .detRun import DetRun
from ..utils import Logger
import glob

class DetSum():
  def __init__(self, folderPath, sumEvery, numMeasurements, startIdx=1, logger=None):
    self.log = Logger() if logger is None else logger
    self.seperateRuns = []

    self.summedMeasurement = []

    for i in range(startIdx, startIdx+numMeasurements):
      run = DetRun(folderPath, self.log, i)
      run.sumDetData(sumEvery)
      self.seperateRuns.append(run)

    for i in range(sumEvery):
      self.summedMeasurement.append(DetData())
      # self.summedMeasurement[i].phi = self.seperateRuns[0].summedData[i].phi
      for j in range(startIdx, startIdx+numMeasurements):
        self.summedMeasurement[i].I += self.seperateRuns[j-startIdx].summedData[i].I
        self.summedMeasurement[i].sI += self.seperateRuns[j-startIdx].summedData[i].sI**2
      self.summedMeasurement[i].sI = np.sqrt(self.summedMeasurement[i].sI)

  # def save(self, filebase):
  #   for i in range(len(self.summedMeasurement)):
  #     with open(f"{filebase}_{i}.dat", 'w') as f:
  #       data = self.summedMeasurement[i]
  #       f.write(self.log.log)
  #       f.write(f"#phi/deg\tI/a.u.\tsI/a.u.\n")
  #       for j in range(len(data.phi)):
  #         f.write(f"{data.phi[j]}\t{data.I[j]}\t{data.sI[j]}\n")