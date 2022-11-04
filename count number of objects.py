#import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load("ps.npy.txt")
labeled = label(image)

mask = np.array([
  np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]]),
  np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1]]),
  np.array([
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]]),
  np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]]),
  np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1]])],
    dtype=object)

all_numbers = 0
numbers =['']
for i in range(0, len(mask)):
  erosion = binary_erosion(labeled, mask[i])
  s = label(erosion).max()
  for j in numbers:
    print("Number of objects: ", s)
    all_numbers += s
print("All number of objects:", all_numbers)

#plt.imshow(labeled)
#plt.show()
