import pyopenms
from collections import Counter
from statistics import mode
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *


exp = pyopenms.MSExperiment()
pyopenms.MzMLFile().load("D:\\4th\\Computational biology\\task1\\BSA1.mzML", exp)
specMass = []
Lmass = []
Masses = []
specIntensity = []
Linten = []
Intensities = []
spec_RT = []
retentionTime = []


# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_xlabel('Mass')
# ax.set_ylabel('Intensity')
# ax.set_zlabel('RT')

# Store the original list of spectrums
for i in range(1600):
    spec = exp[i]
    if spec.getMSLevel() == 1:
        mz, intensity = spec.get_peaks()
        specMass.append(mz)
        specIntensity.append(intensity)
        r = spec.getRT()
        spec_RT.append(r)
        #ax.plot(mz,  intensity, r, zdir='y', color='red')
#plt.savefig("D:\\4th\\Computational biology\\task1\\3d.png")


# filtering Masses, take the first five elements
for m in specMass:
    Lmass.append(m[0:6])

for i in Lmass:
    for j in i:
        Masses.append(j)

# filtering Intensties, take the first five elements
for t in specIntensity:
    Linten.append(t[0:6])

for i in Linten:
    for j in i:
        Intensities.append(j)

# Duplicate RT
retentionTime = [spec_RT[i//6] for i in range(len(spec_RT)*6)]

data = {"Mass": Masses, "Intensity": Intensities, "RT": retentionTime}
DF = pd.DataFrame(data)
DF.to_csv('D:\\4th\\Computational biology\\task1\\Data1.csv')


# Round Masses to the nearest 6 decimal places to easily find the most frequent Mass
Filter_mass = []
for i in Masses:
    Filter_mass.append(format(i, ".5f"))

# find the most frequent mass


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(Filter_mass):
        if value == item_to_find:
            indices.append(idx)
    return indices


mode_index = find_indices(Filter_mass, mode(Filter_mass))
depend_Intensity = []
depend_RT = []

# Store the RT & Intensities based on the most frequent Mass
for i in mode_index:
    depend_Intensity.append(Intensities[i])
    depend_RT.append(retentionTime[i])

data2 = {"Intensity": depend_Intensity, "RT": depend_RT}
DF2 = pd.DataFrame(data2)
DF2.to_csv('D:\\4th\\Computational biology\\task1\\Data2.csv')

# 2d plot
fig = plt.figure()
plt.plot(depend_Intensity, depend_RT)
plt.show()

# heatmap
x = Masses
y = Intensities
z = retentionTime
colo = [x + y + z]
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
color_map = cm.ScalarMappable(cmap=cm.Greens_r)
color_map.set_array(colo)

# creating the heatmap
img = ax.scatter(x, y, z, marker='s',
                 s=200, color='green')
plt.colorbar(color_map)

# adding title and labels
ax.set_title("3D Heatmap")
ax.set_xlabel('Mass')
ax.set_ylabel('Intensity')
ax.set_zlabel('RT')
plt.show()

depend_Intensity0 = []
depend_RT0 = []
Filter_mass0 = []
for i in Masses:
    Filter_mass0.append(int(i))

# find the most frequent mass


# def find_indices(list_to_check, item_to_find):
#     indices = []
#     for idx, value in enumerate(Filter_mass0):
#         if value == item_to_find:
#             indices.append(idx)
#     return indices
for i in Filter_mass0:
    if (Filter_mass0[i] == 300):
        depend_Intensity0.append(Intensities[i])
        depend_RT0.append(retentionTime[i])


# Store the RT & Intensities based on the most frequent Mass


# 2d heatmap
fig = plt.figure()
data = np.random.random((int(depend_Intensity0[0]), int(depend_RT0[0])))
plt.imshow(data, cmap='autumn', interpolation='nearest')

plt.title("2-D Heat Map")
plt.show()
