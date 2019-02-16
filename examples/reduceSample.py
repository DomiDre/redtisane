from redtisane import SummedMeasurement, AveragedRun
import numpy as np
import matplotlib.pyplot as plt

# data = SummedMeasurement('./852Hz_S_TISANE/[]/0.0055/*.AVE', sumEvery=8, numMeasurements=10)
# data = SummedMeasurement('./690Hz_S_TISANE/[]/0.0055/*.AVE', sumEvery=8, numMeasurements=10)
# data = SummedMeasurement('./400Hz_S_TISANE/[]/0.0045/*.AVE', sumEvery=8, numMeasurements=10)
data1 = AveragedRun('./100Hz_S_cont/*.AVE')
data2 = AveragedRun('./200Hz_S_cont/*.AVE')
data3 = AveragedRun('./300Hz_S_cont/*.AVE')
data4 = SummedMeasurement('./400Hz_S_TISANE/[]/0.0045_more/*.AVE', sumEvery=8, numMeasurements=10)

fig, ax = plt.subplots(2,2, sharex=True)
for i in [3,7]:#np.arange(0,8,4):
  ax[0,0].errorbar(
    data1.aveData[i].phi,
    data1.aveData[i].I,
    data1.aveData[i].sI,
    label=f'100 Hz Slice {i}')
ax[0,0].legend(fontsize=8)


for i in [3,7]:#np.arange(0,8,4):
  ax[0,1].errorbar(
    data2.aveData[i].phi,
    data2.aveData[i].I,
    data2.aveData[i].sI,
    label=f'200 Hz Slice {i}')
ax[0,1].legend(fontsize=8)


for i in [3,7]:#np.arange(0,8,4):
  ax[1,0].errorbar(
    data3.aveData[i].phi,
    data3.aveData[i].I,
    data3.aveData[i].sI,
    label=f'300 Hz Slice {i}')
ax[1,0].legend(fontsize=8)


for i in [3,7]:
  ax[1,1].errorbar(
    data4.summedMeasurement[i].phi,
    data4.summedMeasurement[i].I,
    data4.summedMeasurement[i].sI,
    label=f'400 Hz Slice {i}')
ax[1,1].legend(fontsize=8)
plt.show()


