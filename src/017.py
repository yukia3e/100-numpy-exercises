#!/usr/bin/python
# 17. What is the result of the following expression?
import numpy as np

print("0 * np.nan")
print(0 * np.nan)

print("np.nan == np.nan")
print(np.nan == np.nan)

print("np.inf > np.nan")
print(np.inf > np.nan)

print("np.nan - np.nan")
print(np.nan - np.nan)

print("np.nan in set([np.nan])")
print(np.nan in set([np.nan]))

print(0.3 == 3 * 0.1)
