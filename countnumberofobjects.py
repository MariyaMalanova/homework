#import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

image = np.load("ps.npy.txt")
labeled = label(image)

mask3 = np.array([
  np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]),
  np.array([
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]]),
  np.array([
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]])],
    dtype=object)

mask1 = np.array([
  np.array([
    [1, 1, 1, 1, 1 ],
    [1, 1, 1, 1, 1 ],
    [1, 0, 0, 0, 1 ],
    [1, 0, 0, 0, 1]]),
  np.array([
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]])],
    dtype=object)
     
mask2 = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]])

all_numbers = 0
numbers =[0]
erosion2 = binary_erosion(labeled, mask2)
k = label(erosion2).max()

for i in range(0, len(mask3)):
  erosion = binary_erosion(labeled, mask3[i])
  all3 = label(erosion).max()
  for j in numbers:
    print("Number of objects: ", all3)
    all_numbers += all3
    
for i in range(0, len(mask1)):
  erosion = binary_erosion(labeled, mask1[i])
  s = label(erosion).max()
  all1 = s - k
  for j in numbers:
    print("Number of objects: ", all1)
    all_numbers += all1
print("All number of objects:", all_numbers)

#plt.imshow(labeled)
#plt.show()
