#!/usr/bin/python
# 13. Create a 10x10 array with random values
# and find the minimum and maximum values
import numpy as np

x = np.random.random((10, 10))
print(x)

min, max = x.min(), x.max()
print(f"min: {min}, max: {max}")
