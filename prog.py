#!/usr/bin/python
from math import *
import numpy as np
import matplotlib.pyplot as plt # allow to draw graphs


########################
# Initialize constants #
########################

def init():
    global x
    global u
    global A
    global B
    global epsilon    
    global NT
    global dT
    global ro
    global w

    T = 1
    w = 2*pi/T
    epsilon=10**(-3)
    NT = 500
    dT = 0.01
    ro = 0.01

    x = np.transpose(np.atleast_2d([0.1,0,0,0]))
    u = np.transpose(np.atleast_2d([0,0]))

    A = np.matrix([[0, 1, 0, 0],
                  [(w**2)*3, 0, 0, 2*w], 
                  [0, 0, 0, 1], 
                  [0, -2*w, 0, 0]])

    B = np.matrix([[0, 0], 
                   [1, 0], 
                   [0, 0], 
                   [0, 1]])



#############################
# Change coords for display #
#############################

def newCoordX(x, y, n):
    global w
    global dT

    return x*cos(w*n*dT) - y*sin(w*n*dT) + cos(w*n*dT)

def newCoordY(x, y, n):
    global w
    global dT
    return x*sin(w*n*dT) + y*cos(w*n*dT) + sin(w*n*dT)


############################
# Solve the first equation #
############################

def calculateF():
    global A
    global x
    global B
    global u
    return A.dot(x) + B.dot(u)

def firstEquation():
    global NT
    global x    
    global dT
    global xTab

    for i in range(0, NT):
        valeur = calculateF()
        x = x+dT*valeur 
        xTab.append(x)
    return x


#############################
# Solve the second equation #
#############################

def calculateG():
    global A
    global x
    global B
    global u

    return np.transpose((-1)*A).dot(x)

def secondEquation():
    global x
    global dT
    global NT
    global pTab
    p = x
    for i in range(0, NT):
        valeur = calculateG()
        p = p - dT * valeur
        pTab.append(p)
    return x

############
# Gratient #
############

def gradient():
    global x
    global u
    global B
    global epsilon    
    
    return epsilon*u + np.transpose(B).dot(x)

def gradientIteration():
    global u
    global ro
    global epsilon    
    global uTab
    global B

    
    for i in range(0, NT):
        u = u - ro * gradient()
        uTab.append(u)
    return u


########
# Main #
########

def main():
    init()
    
    global xTab
    global pTab
    global uTab
    xTab = []
    pTab = []
    uTab = []

    firstEquation()
    secondEquation()
    gradientIteration()

    x1 = []
    y1 = []
    for i in range(0, len(xTab)):
        x1.append(newCoordX(xTab[i][0, 0], xTab[i][2, 0], i))
        y1.append(newCoordY(xTab[i][0, 0], xTab[i][2, 0], i))

    plt.plot(x1, y1)
    plt.show()


if __name__=='__main__' :
    main()
