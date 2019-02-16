from ..utils import Logger
import numpy as np

class AveData:
  def __init__(self, avefile=None, logger=None):
    # Init variables
    self.log = Logger() if logger is None else logger
    self.phi  = 0
    self.I    = 0
    self.sI   = 0
    self.parameters = {}

    if avefile is not None:
      # Load file
      self.load_file(avefile)


  def read_param_line(self, f, paramName):
    line = next(f)
    value = line.split(':', 1)[-1].strip()
    self.parameters[paramName] = value

  def load_file(self, datafile):
    # self.log.printLog(f"Loading {datafile}")
    with open(datafile, 'r') as f:
      next(f)
      line = next(f)
      self.parameters['sampleName'] = line.split(':', 1)[-1].strip()

      next(f)
      line = next(f)
      parameterValues = line.split()
      self.parameters['monCnt']      = float(parameterValues[0])
      self.parameters['wavelength']  = float(parameterValues[1])
      self.parameters['detAng']      = float(parameterValues[2])
      self.parameters['detDist']     = float(parameterValues[3])
      self.parameters['trans']       = float(parameterValues[4])
      self.parameters['thickness']   = parameterValues[5]
      self.parameters['aveStep']     = float(parameterValues[6])

      next(f)
      line = next(f)
      parameterValues = line.split()
      self.parameters['BCENT(X)']    = float(parameterValues[0])
      self.parameters['BCENT(Y)']    = float(parameterValues[1])
      self.parameters['A1(mm)']      = float(parameterValues[2])
      self.parameters['A2(mm)']      = float(parameterValues[3])
      self.parameters['A1A2DIST(m)'] = float(parameterValues[4])
      self.parameters['DL/L']        = float(parameterValues[5])
      self.parameters['BSTOP(mm)']   = float(parameterValues[6])
      self.parameters['DET_TYP ']    = parameterValues[6]

      self.read_param_line(f, 'SAM')
      self.read_param_line(f, 'BGD')
      self.read_param_line(f, 'EMP')
      self.read_param_line(f, 'DIV')
      self.read_param_line(f, 'MASK')
      self.read_param_line(f, 'ABS Parameters (3-6)')
      self.read_param_line(f, 'Average Choices')

      next(f)
      phi = []
      I = []
      sI = []
      for line in f:
        split_line = line.strip().split()
        phi.append(float(split_line[0]))
        I.append(float(split_line[1]))
        sI.append(float(split_line[2]))
      self.phi = np.array(phi)
      self.I = np.array(I)
      self.sI = np.array(sI)