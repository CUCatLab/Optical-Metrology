import matplotlib.pyplot as plt
import numpy as np

#this is the simualtion code for a set up with 2 polarizing beam splitters, 4 HWPs, 1 polarizer, 1 normal beamsplitter, and a mirror

#polarization x1= polarization angle one
#polarization x2= polarization angle two

________________________________________________________________________________________________________________________________________________

def bs(x1,n =.1):
    "gives light after going through HWP BS setup"
    p = np.array([[np.sqrt(1-n**2), 0],[0, n]]) #polarization of beamsplitter
    HWP  = np.array([np.cos(x)**2 - np.sin(x)**2, 2*np.cos(x)*np.sin(x)], [2*np.cos(x)*np.sin(x), np.sin(x)**2 - np.cos(x)**2]) #half waveplate matrix
    THWP = HWP.transpose() # transpose of HWP matrix
    #matrix multiplication
    bs  = THWP @ p @ HWP
    #print resulted matrix
    return(bs)

"Do I need the rotation matrix anymore since the HWP matrix accounts for rotation angles????????????????????????????????????????????????????????????"

_____________________________________________________________________________________________________________________________________________


def ID(x1,x3,x4,thetamin = 135, thetamax = 145):
    "gives the intensity going to the dark port"
    L = np.array([1,0])
    acw = bs(x1,n=.1)
    accw = bs(-x1,n=.1)
    ccw = bs(x3,n=.1)
    cccw = bs(-x3,n=.1)
    d = bs(x4,n=0)
    DI = []
    x2s = np.arange(thetamin,thetamax,.1)

    for x2 in x2s:
        bcw = bs(x2,n=.1)
        bccw = bs(-x2,n=.1)
        A = ((cccw@ bccw@ accw -acw@ bcw@ ccw)/2)
        B = ((accw@ bccw@ cccw-ccw@ bcw@ acw)/2)
        C = (L@(A)@ d@ (B)@ L)
        DI.append(C)

    return(x2s,np.array(DI))

def IB(x1,x3,x4,thetamin = 135, thetamax = 145):
    "gives the intensity going to the bright port"
    L = np.array([1,0])
    acw = bs(x1,n=.1)
    accw = bs(-x1,n=.1)
    ccw = bs(x3,n=.1)
    cccw = bs(-x3,n=.1)
    d = bs(x4,n=0)
    BI = []
    x2s = np.arange(thetamin,thetamax,.1)

    for x2 in x2s:
        bcw = bs(x2,n=.1)
        bccw = bs(-x2,n=.1)
        B = ((ccw@ bcw@ acw+accw@ bccw@ cccw)/2)
        A = ((acw@ bcw@ ccw+ cccw@ bccw@ accw)/2)
        C = (L@(A)@ d@(B)@ L)
        BI.append(C)

    return(x2s,np.array(BI))




def bright(x1,x3,x4,thetamin = 135, thetamax = 145):
    "this plots the the light coming out of the bright port"
    x2s,Br = IB(x1,x3,x4,thetamin, thetamax)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Br,color="purple")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$I_b/I_0$')
    plt.title('Bright Port Intensity vs Polarizer Angle')
    #plt.ylim((.02,.08))
    plt.grid(True)
    plt.xlim((thetamin,thetamax))
    plt.show()
    return(f)

def dark(x1,x3,x4,thetamin = 135, thetamax = 145):
    "this plots the the light coming out of the darkport"
    x2s,Da = ID(x1,x3,x4,thetamin, thetamax)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Da,color="k")
    plt.xlabel(r"$\phi$ (deg)")
    plt.ylabel(r"$I_d/I_0$")
    plt.title("Dark Port Intensity vs Polarizer Angle")
    #plt.ylim((.02,.08))
    plt.grid(True)
    plt.xlim((thetamin,thetamax))
    plt.show()
    return(f)

def split(x1,x3,x4,thetamin = 135, thetamax = 145):
    "bright port minus dark"

    x2s,Br = IB(x1,x3,x4,thetamin, thetamax)
    x2s,Da = ID(x1,x3,x4,thetamin, thetamax)
    s = Da-Br / (Br+Da)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,s,color="k")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$(I_d-I_b)/(I_b+I_d)$')
    plt.title('Intensity Difference')
    #plt.ylim((-1,0.25))
    plt.xlim((thetamin,thetamax))
    plt.grid(True)
    plt.show()
    return(f)





