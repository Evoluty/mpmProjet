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
    global uTab

    T = 1.0
    w = 2*pi/T
    epsilon=0.001
    NT = 500
    dT = T/NT
    ro = 0.03

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

    uTab = []
    for i in range(0, NT):
        uTab.append(u)


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

def calculateF(i):
    global A
    global uTab
    global B
    global u
    return A.dot(x) + B.dot(uTab[i])

def firstEquation():
    global NT
    global x    
    global dT
    global xTab

    for i in range(0, NT):
        valeur = calculateF(i)
        x = x+dT*valeur 
        xTab.append(x)
    return x


#############################
# Solve the second equation #
#############################

def calculateG(i):
    global A
    global xTab
    global B
    global u

    return np.transpose((-1)*A).dot(xTab[i])

def secondEquation():
    global x
    global dT
    global NT
    global pTab
    p = x
    for i in range(0, NT):
        valeur = calculateG(i)
        p = p - dT * valeur
        pTab.append(p)
    return p

############
# Gratient #
############

def gradient():
    global x
    global u
    global B
    global epsilon    
    
    return epsilon*u + np.transpose(B).dot(x)

def gradientIteration(i):
    global u
    global ro
    global epsilon    
    global uTab
    global B

    u = uTab[i] - ro * gradient()
    uTab.append(u)
    return u


########
# Main #
########

def main():
    init()
    
    global dT
    global xTab
    global pTab
    global uTab
    global NT

    for i in range(0, NT):
        xTab = []
        pTab = []
        x = np.transpose(np.atleast_2d([0.1,0,0,0]))
        firstEquation()
        secondEquation()
        for j in range (0, NT):
            uTab.append(np.transpose(np.atleast_2d([0,0])))
            gradientIteration(j)
        

    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(0, len(xTab)):
        x1.append(newCoordX(xTab[i][0, 0], xTab[i][2, 0], i))
        y1.append(newCoordY(xTab[i][0, 0], xTab[i][2, 0], i))

        x2.append(cos(w*i*dT))
        y2.append(sin(w*i*dT))

    plt.plot(x1, y1)
    # plt.plot(x2,y2)
    plt.show()


if __name__=='__main__' :
    main()
