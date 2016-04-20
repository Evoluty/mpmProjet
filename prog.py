import numpy as np
import sys
from math import *
from scipy import *
from scipy.integrate import odeint # Pour resoudre l equation differentielle
import matplotlib.pyplot as plt # Permet de tracer des graphes

x = 0
u = 0
A = 0
B = 0
epsilon = 0
NT = 0
dT = 0


def init():
    # definition des vecteurs x et u
    global x
    x = np.array([1, 0, 0, 0])
    global u
    u = np.array([0, 0])

    T = 5480
    w = 2*pi/T

    global A
    A = np.matrix([[0, 1, 0, 0], [(3*w)**2, 0, 0, 2*w], [0, 0, 0, 1], [0, -2*w, 0, 0]])

    global B
    B = np.matrix([[0, 0], [1, 0], [0, 0], [0, 1]])
    global epsilon
    epsilon=10**(-8)
    global NT
    NT = 1000
    global dT
    dT = 0.1


def fun():
    return np.dot(A, x.transpose()) + np.dot(B, u.transpose()) 

def euler():
    for i in range(0, NT)
        valeur = fun()
        x = x+dT*valeur
        t = t+dT
    return x

def deuxFun():
    return np.dot(A, x.transpose()) + np.dot(B, u.transpose()) 

def main():
    init()
    # print A
    # pas = 200
    # ro = 0.1
    # for i in range(0, pas):
    #     u = u - ro * grad(u)
    
    diffx()
    plt.plot(x[0], x[2])
    plt.show()




if __name__=='__main__' :
    main()
