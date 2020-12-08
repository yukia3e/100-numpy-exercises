#!/usr/bin/python
# 15. Create a 2d array with 1 on the border and 0 inside
import numpy as np

x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)
