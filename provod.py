import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion

mask = [[0,1,0],
        [0,1,0],
        [0,1,0]]
image = np.load("C:\\Users\\manka\\Desktop\\less\\wires6.npy.txt")
labeled = label(image)
for i in range(1,labeled.max()+1):
    one_wire = np.zeros_like(image)
    one_wire[labeled==i] = 1
    empty = binary_erosion(one_wire,mask)
    empty_labeled = label(empty)
    if empty_labeled.max() in [2,3,4]:
        print( i , "провод разделен на ", empty_labeled.max(), "части")
    elif empty_labeled.max() == 1:
        print(i , " провод не разделен ")
    elif empty_labeled.max() == 0:
        print( i , "провод не является проводом, т.к. его толщина <> 3 пикселам")
    else:
        print( i , "провод разделен на ", empty_labeled.max(), "частей")
plt.imshow(labeled)
plt.show()