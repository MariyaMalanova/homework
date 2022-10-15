import numpy as np
import matplotlib.pyplot as plt

def check(B, y, x):
  if not 0 <= x < B.shape[1]:
    return False
  if not 0 <= y < B.shape[0]:
    return False
  if B[y, x] != 0:
    return True
  return False

def neighbours2(image, y, x): 
  left = y, x-1
  top = y-1, x
  if not check(image, *left):
    left = None
  if not check(image, *top):
    top = None
  return left, top

def find(label, linked):
  j = label
  while linked[j] != 0:
    j = linked[j]
  return j

def union(label1, label2, linked):
  j = find(label1, linked)
  k = find(label2, linked)
  if j != k:
    linked[k] = j

def two_pass_labeling(binary_image):
    labels = np.zeros_like(binary_image)
    label = 1 
    linked = np.zeros(len(binary_image), dtype='uint') 
    for y in range(len(binary_image)):
        for x in range(binary_image.shape[0]):
            if binary_image[y, x] != 0:
                ns = neighbours2(binary_image, y, x)
                if ns[0] is None and ns[1] is None:
                  m = label
                  label += 1
                else:
                  lbs = [labels[i] for i in ns if i is not None]
                  m = min(lbs) 
                labels[y, x] = m
                for n in ns:
                  if n is not None:
                    lb = labels[n]
                    if lb != m:
                      union(m, lb, linked)
    for y in range(binary_image.shape[0]):
      for x in range(binary_image.shape[1]):
        if binary_image[y, x] != 0:
          new_label = find(labels[y, x], linked)
          if new_label != labels[y, x]:
            labels[y, x] = new_label
    return labels

def count_in_right_way(labels):
  dtd = {}
  i = 1
  for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
      if labels[y, x] in dtd:
        labels[y, x] = dtd[labels[y, x]]
      elif labels[y, x] != 0 and labels[y, x] not in dtd:
        dtd.update({labels[y, x] : i})
        i += 1
  print(dtd)
  return labels

if __name__ == "__main__":
    image = np.zeros((20, 20), dtype='int32')
    
    image[1:-1, -2] = 1
    
    image[1, 1:5] = 1
    image[1, 7:12] = 1
    image[2, 1:3] = 1
    image[2, 6:8] = 1
    image[3:4, 1:7] = 1
    
    image[7:11, 11] = 1
    image[7:11, 14] = 1
    image[10:15, 10:15] = 1
    
    image[5:10, 5] = 1
    image[5:10, 6] = 1

    labeled_image = two_pass_labeling(image)
    
    print("Labels - ", list(set( labeled_image.ravel()))[1:])
    
    
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(image, cmap="hot")
    plt.colorbar(ticks=range(int(2)))
    plt.axis("off")
    plt.subplot(122)
    plt.imshow( labeled_image.astype("uint8"), cmap="hot")
    plt.colorbar()
    plt.axis("off")
    plt.tight_layout()
    plt.show()