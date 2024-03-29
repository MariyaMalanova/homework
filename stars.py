import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

stars = np.load("stars.npy")
labeled = label(stars)

mask = [[0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],]

mask2 = [[1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],]

er = binary_erosion(labeled, mask)
er = label(er)

er2 = binary_erosion(labeled, mask2)
er2 = label(er2)

print(er.max())
print(er2.max())

plt.imshow(stars)
plt.show()
