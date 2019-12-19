

#Attempting to simulate 6 different states of light as they go through waveplates and beamsplitters
#Incoming light is horizontally polarized

import numpy as np
import pandas as pd




def HWP(x):
    # Half Wave Plate shifts the polarization direction of linearly polarized light can get Horizantal, Vertical, Diagonal, and Antidiagonal states from this
    H = np.array([[np.cos(2*x), np.sin(2*x)], [np.sin(2*x), -np.cos(2*x)]])
    return (H)

def QWP(y):
    #Changes linearly polarized light to circular or eliptically polarized light can get right and left circularly polarized light out of this
    Q = np.array([[(np.cos(y)**2) +(1j*np.sin(y)**2),  ((1-1j)*np.sin(y)*np.cos(y))], [((1-1j)*np.sin(y)*np.cos(y)), (1j*np.cos(y)**2) +(np.sin(y)**2)]])
    return(Q)

def Polarization(x,y):
    #uses the results from the HWP and QWP to obtain light final polarization before going through the beam splitter
    h = np.array([1,0])
    H = HWP(x)
    Q = QWP(y)
    P0 = Q@ h
    P = P0@ H
    a = P[0]
    b = P[1]
    list = [a,b]
    return (list)


# having an incomplete func causes an error when trying to run the code in Jupyter

def BeamSplitter(list):
    # splits the light in two different directions each split of light is one of the pairs of states... (want to take the matrix mupltiplication of the results of the function above and imput here polarization of light)

    A = np.array(list)
    print(A)
    d = np.array([(1/a),0])
    Z = d@ A
    T = d@ B
    return (Z,T)












