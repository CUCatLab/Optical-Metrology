#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

#this is the simualtion code for a set up with 2 polarizing beam splitters, 4 HWPs, 1 polarizer, 1 normal beamsplitter, and a mirror

#polarization x1= polarization rotation angle one
#polarization x2= polarization rotation angle two
#polarization x3= polarization rotation angle three

"________________________________________________________________________________________________________________________________________________"
# Half Waveplate function
# x = rotation angle of HWP
def HWP(x1):
    hwp = np.array(([np.cos(x1)**2 - np.sin(x1)**2, 2*np.cos(x1)*np.sin(x1)], [2*np.cos(x1)*np.sin(x1), np.sin(x1)**2 - np.cos(x1)**2])) #half waveplate matrix
# simplifiy HWP with trig identities
    return(hwp)

# polarizer with leakage
def pol(n=.1):
    hp = np.array([[np.sqrt(1-n**2), 0],[0, n]]) #polarizer
    return(hp)

def PHWP(x1,n = .1):
    hwp = np.array(([np.cos(x1)**2 - np.sin(x1)**2, 2*np.cos(x1)*np.sin(x1)], [2*np.cos(x1)*np.sin(x1), np.sin(x1)**2 - np.cos(x1)**2]))
    p = pol(n)
    Thwp = hwp.transpose()
    PHW = Thwp @ pol(n) @ hwp

# polarizer on rotation mount
def rm(x1,n=.1):
    RM = np.array([[np.cos(np.deg2rad(x1)),-np.sin(np.deg2rad(x1))],[np.sin(np.deg2rad(x1)),np.cos(np.deg2rad(x1))]])
    p = pol(n=n)
    RMT = RM.transpose()
    R = RM @ p @ RMT
    return(R)


def intensity(x1,x3,thetamin, thetamax, x4):
    
    #make a function that spits out whatever your lights going to be depending on polarization (nothing should be set since we can )
    "gives the intensity going to the dark port"
    L = np.array([1,0]) # laser light going into interferometer horizonatlly polarized
    acw = HWP(-x1) @ pol(n=.1) @ HWP(x1) # polarizer 1 with light coming in at a clockwise direction ( HWP @ pol@ )make sure both HWP can have dif angles
    accw = HWP(x1) @ pol(n=.1) @ HWP(-x1) # polarizer 1 with light coming in at a counterclockwise direction
    ccw = HWP(-x3) @ pol(n=.1) @ HWP(x3) # polarizer 3 with light coming in at a clockwise direction
    cccw = HWP(x3) @ pol(n=.1) @ HWP(-x3) # polarizer 3 with light coming in at a counterclockwise direction
    d = rm(x4,n=0) # perfect polarizer between exiting light and detector
    DI = [] # darkport intensity
    x2s = np.arange(thetamin,thetamax,.1) # making an array of all the different rotation angles of polarizer between set max and min angles

    
    for x2 in x2s: 
        "iterating over all the different angles to get insentities at that set angle and putting the intensities into a list"
        bcw = rm(x2,n=.1) # polarizer 2 with light coming in at a clockwise direction
        bccw = rm(-x2,n=.1) # polarizer 2 with light coming in at a counterclockwise direction
        B = ((accw@ bccw@ cccw-ccw@ bcw@ acw)/2)
        A = B.transpose()
        C = (L@(A) @d @ (B)@ L)
        DI.append(C)
    
    
    return(x2s,np.array(DI))


def vertical(x1,x3,thetamin, thetamax):
    "this plots the the vertical light coming out of the dark port"
    x2s,Vt = intensity(x1,x3,thetamin, thetamax,x4 =90)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Vt,color="purple")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$I_b/I_0$')
    plt.title('Vertical Dark Port Intensity vs Polarizer Angle')
    plt.grid(True)
    plt.xlim((thetamin,thetamax))
    plt.show()
    return(f)

def horizontal(x1,x3,thetamin, thetamax ):
    "this plots the horizontal light coming out of the darkport"
    x2s,Hz = intensity(x1,x3, thetamin, thetamax,x4 =0)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Hz,color="magenta")
    plt.xlabel(r"$\phi$ (deg)")
    plt.ylabel(r"$I_d/I_0$")
    plt.title("Horizontal Dark Port Intensity vs Polarizer Angle")
    plt.grid(True)
    plt.xlim((thetamin,thetamax))
    plt.show()
    return(f)

def split(x1,x3,thetamin, thetamax):
    "bright port minus dark ratio to total initial intensity"

    x2s,Vt = intensity(x1,x3,thetamin, thetamax,x4= 90)
    x2s,Hz = intensity(x1,x3,thetamin, thetamax,x4= 0 )
    s = Vt-Hz / (Hz+Vt)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,s,color="aqua")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$(I_d-I_b)/(I_b+I_d)$')
    plt.title('Intensity Difference')
    plt.xlim((thetamin,thetamax))
    plt.grid(True)
    plt.show()
    return(f)


# In[2]:


# Intesity going to darkport

x1 = 10
x3 = -40
thetamin=0
thetamax = 180


DP = horizontal(x1,x3,thetamin, thetamax)
DP.savefig("DP.png",dpi=600,pad_inches= 0.25,bbox_inches="tight")
# Intesity going to brightport

BP = vertical(x1,x3,thetamin, thetamax)
BP.savefig("BP.png",dpi=600,pad_inches=0.25,bbox_inches="tight")

SP = split(x1,x3,thetamin, thetamax)
SP.savefig("SP.png", dpi=600,pad_inches=0.25,bbox_inches="tight")


# In[3]:


# this last difference of intensity plot shouldnt have anything in the negative check the math in your code to make sure its correct!

