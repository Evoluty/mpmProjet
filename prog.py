#!/usr/bin/python
from math import *
import numpy as np
import matplotlib.pyplot as plt # allow to draw graphs


########################
# Initialize constants #
########################


T = 1.0
w = (2*pi)/T
epsilon=0.001
NT = 500
dT = T/NT
ro = 0.03

x = np.transpose(np.atleast_2d([0.1, 0.,0.,0.]))
u = np.transpose(np.atleast_2d([0.,0.]))

A = np.mat([[0., 1., 0., 0.],
              [(w**2)*3., 0., 0., 2.*w], 
              [0., 0., 0., 1.], 
              [0., -2*w, 0., 0.]])

B = np.mat([[0., 0.], 
               [1., 0.], 
               [0., 0.], 
               [0., 1.]])


#############################
# Change coords for display #
#############################

def newCoordX(xk, yk, n):
    return xk*cos(w*n*dT) - yk*sin(w*n*dT) + cos(w*n*dT)

def newCoordY(xk, yk, n):
    return xk*sin(w*n*dT) + yk*cos(w*n*dT) + sin(w*n*dT)


############################
# Solve the first equation #
############################

def calculateF(xk, uk):
    return np.dot(A, xk) + np.dot(B, uk)

def firstEquation(xk, uk):
    xTab = [xk]
    for i in range(0, NT):
        valeur = calculateF(xk, uk)
        xk = xk+dT*valeur 
        xTab.append(xk)
    return xTab


#############################
# Solve the second equation #
#############################

def calculateG(p):
    return -np.dot(A.T, p)

def secondEquation(p):
    pTab = [p]
    for i in range(0, NT):
        valeur = calculateG(p)
        p = p - dT * valeur
        pTab.append(p)
    return pTab

############
# Gratient #
############

def gradient(p):    
    return epsilon*u + np.dot(B.T, p)


########
# Main #
########

def main():
    k = u
    for i in range(0, NT):
        xTab = firstEquation(x, k)
        pTab = secondEquation(xTab[NT])
        grad = gradient(pTab[NT-i])
        k=k-ro*grad        

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(0, NT):
        x1.append(newCoordX(float(xTab[i][0][0]), float(xTab[i][2][0]), i))
        y1.append(newCoordY(float(xTab[i][0][0]), float(xTab[i][2][0]), i))

        x2.append(cos(w*i*dT))
        y2.append(sin(w*i*dT))

    plt.plot(x1, y1)
    plt.plot(x2,y2)
    plt.show()


if __name__=='__main__' :
    main()
