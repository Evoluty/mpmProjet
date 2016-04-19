import numpy as np

x1 = 0
xp1 = 0
x2 = 0
xp2 = 0
x = np.array([x1, xp1, x2, xp2])

u1 = 0
u2 = 0
u = np.array([u1, u2])

w = 0
A = np.matrix([[0, 1, 0, 0], [(3*w)**2, 0, 0, 2*w], [0, 0, 0, 1], [0, -2*w, 0, 0]])

B = np.matrix([[0, 0], [1, 0], [0, 0], [0, 1]])


