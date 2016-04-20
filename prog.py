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
    epsilon=10**(-8)
    NT = 50
    dT = 0.01
    ro = 0.03

    x = np.transpose(np.atleast_2d([1,0,0,0]))
    u = np.transpose(np.atleast_2d([0,0]))

    A = np.matrix([[0, 1, 0, 0],
                  [w**2*3, 0, 0, 2*w], 
                  [0, 0, 0, 1], 
                  [0, -2*w, 0, 0]])

    B = np.matrix([[0, 0], 
                   [1, 0], 
                   [0, 0], 
                   [0, 1]])


############################
# Solve the first equation #
############################

def changement_coord_x1(x1, x2, n, delta_t):
    global w
    return x1*cos(w*n*delta_t) - x2*sin(w*n*delta_t) + cos(w*n*delta_t)

def changement_coord_x2(x1, x2, n, delta_t):
    global w
    return x1*sin(w*n*delta_t) + x2*cos(w*n*delta_t) + sin(w*n*delta_t)

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
    global tab_x

    for i in range(0, NT):
        valeur = calculateF()
        print x
        x = x+dT*valeur 
        tab_x.append([changement_coord_x1(x[0,0], x[2,0], i, dT), x[1,0], changement_coord_x2(x[0,0], x[2,0], i, dT), x[3,0]])
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
    p = firstEquation()    
    global dT
    global NT
    
    for i in range(0, NT):
        valeur = calculateG()
        p = p - dT * valeur
    return p

############
# Gratient #
############

def gradient():
    global u
    global B
    global epsilon    
    return epsilon*u + np.transpose(B).dot(secondEquation())

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
    
    global tab_x
    tab_x = []

    print gradientIteration()

    global x
    print "test"
    print x
    x1 = []
    y1 = []
    for i in range(0, len(x)):
        x1.append(tab_x[i][0])
        y1.append(tab_x[i][2])

    plt.plot(x1, y1)
    plt.show()


if __name__=='__main__' :
    main()
