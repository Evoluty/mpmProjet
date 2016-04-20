import numpy as np
import sys
from math import *

# definition des vecteurs x et u
x = np.array([1, 0, 0, 0])
u = np.array([0, 0])

T = 5480
w = 2*math.pi/T
A = np.matrix([[0, 1, 0, 0], [(3*w)**2, 0, 0, 2*w], [0, 0, 0, 1], [0, -2*w, 0, 0]])
B = np.matrix([[0, 0], [1, 0], [0, 0], [0, 1]])
