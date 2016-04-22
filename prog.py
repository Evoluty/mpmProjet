#!/usr/bin/python
from math import *
import numpy as np # allow matrix 
import matplotlib.pyplot as plt # allow to draw graphs


print "Program starts"


########################
# Initialize constants #
########################

print "Initialize constants"

T = 1.0
w = 2*pi/T
epsilon=10**-3
NT = 500
dT = T/NT
ro = 0.03

x = np.transpose(np.atleast_2d([0.1, 0, 0, 0]))
u = np.transpose(np.atleast_2d([0, 0]))

A = np.matrix([[0, 1, 0, 0],
              [3*(w**2), 0, 0, 2*w], 
              [0, 0, 0, 1], 
              [0., -2*w, 0, 0]])

B = np.matrix([[0, 0], 
               [1, 0], 
               [0, 0], 
               [0, 1]])


############################
# Change coords to display #
############################

# Returns the xCoord on circular axes
def newCoordX(xk, yk, n):
    return xk*cos(w*n*dT) - yk*sin(w*n*dT) + cos(w*n*dT)

# Returns the yCoord on circular axes
def newCoordY(xk, yk, n):
    return xk*sin(w*n*dT) + yk*cos(w*n*dT) + sin(w*n*dT)


############################
# Solve the first equation #
############################

# Returns xk : the solution of the current step of the euler equation
def calculateF(xk, uk):
    return np.dot(A, xk) + np.dot(B, uk)

# Returns xn : the array of the solutions of the euler equation
def firstEquation(xk, uk):
    xTab=[xk]
    for k in range(0, NT):
        res=calculateF(xk,uk)
        xk = xk+dT*res
        xTab.append(xk)
    return xTab


#############################
# Solve the second equation #
#############################

# Returns pk : the solution of the current step of the backward euler equation
def calculateG(p):
    return np.dot(-1*A.T, p)

# Returns pn : the array of the solutions of the backward euler equation
def secondEquation(p):
    pTab=[p]
    for k in range(0, NT):
        res=calculateG(p)
        p = p-dT*res
        pTab.append(p)
    return pTab


############
# Gratient #
############

# Returns uk : the current gradient value
def gradient(p):    
    return epsilon*u + np.dot(B.T, p)


########
# Main #
########

# Iterates and call the other functions
def main():
    # Uses the global u vector
    global u
    # Iterates and call the functions to get closer and closer to the best solution
    print "Starts iterating"
    for i in range(0, NT):
        if (i%50 == 0):
            print "Iteration number " + str(i)
        xTab = firstEquation(x, u)
        pTab = secondEquation(xTab[NT])
        grad = gradient(pTab[NT-i])
        # We initialize the next u
        u=u-ro*grad        

    # Put the results in tabs and modify the values to put them in the circular base
    print "Retrieving values" 
    x1, y1, x2, y2 = [], [], [], []
    for i in range(0, NT):
        # These arrays represent the mouvement of the rocket
        x1.append(newCoordX(float(xTab[i][0][0]), float(xTab[i][2][0]), i))
        y1.append(newCoordY(float(xTab[i][0][0]), float(xTab[i][2][0]), i))
        # Second array is to print the circular mouvement of the ISS Station 
        x2.append(cos(w*i*dT))
        y2.append(sin(w*i*dT))

    # Prints the results
    print "Printing values"
    plt.plot(x1, y1)
    plt.plot(x2,y2)
    plt.show()
    print "End of program"

# Calls the main function if the code is called as a program
if __name__=='__main__' :
    main()
