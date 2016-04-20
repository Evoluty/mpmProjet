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

    T = 5480
    w = 2*pi/T
    epsilon=10**(-8)
    NT = 1000
    dT = 0.1
    ro = 0.1

    x = np.array([1, 0, 0, 0])
    u = np.array([0, 0])

    A = np.matrix([[0, 1, 0, 0], [(3*w)**2, 0, 0, 2*w], [0, 0, 0, 1], [0, -2*w, 0, 0]])
    B = np.matrix([[0, 0], [1, 0], [0, 0], [0, 1]])


############################
# Solve the first equation #
############################

def calculateF():
    global A
    global x
    global B
    global u

    return np.dot(A, x.transpose()) + np.dot(B, u.transpose()) 

def firstEquation():
    global NT
    global x    

    for i in range(0, NT):
        valeur = calculateF()
        x = x+dT*valeur
    return x


#############################
# Solve the second equation #
#############################

def calculateG():
    global A
    global x
    global B
    global u

    return np.dot(np.transpose((-1)*A), x)

def secondEquation():
    global x    
    global dT
    global NT

    for i in range(0, NT):
        valeur = calculateG()
        x = x - dT * valeur
    return x

############
# Gratient #
############

def gradient():
    global u
    global B
    global epsilon    

    return np.dot(epsilon*u + B, secondEquation())

def gradientIteration():
    global u
    global ro
    global epsilon    
    global B

    for i in range(0, NT):
        u = u - ro * gradient()
    return u


########
# Main #
########

def main():
    init()
    
    x1 = []
    y1 = []

    gradientIteration()

    global x
    for i in range(0, len(x)):
        x1.append(x[i][0])
        y1.append(x[i][2])

    plt.plot(x, y)
    plt.show()


if __name__=='__main__' :
    main()
