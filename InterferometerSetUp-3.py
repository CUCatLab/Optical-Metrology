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
    # why did i need extra parenthases for np.array to understan the data type??????????????????????

    return(hwp)

# horizontal polarizer with leakage
def HPL(n=.1):
    hp = np.array([[np.sqrt(1-n**2), 0],[0, n]]) #horizontal polarizer
    return(hp)

# polarizer setup of 2 HWP and 1 PBS
def pol(x1,n =.1):
    hwp = HWP(x1)
    hp = HPL(n)
    p  = hwp.transpose()@ hp@ hwp
    return(p)

"_____________________________________________________________________________________________________________________________________________"


def ID(x1,x3,x4,thetamin = 135, thetamax = 145):
    "gives the intensity going to the dark port"
    L = np.array([1,0])
    acw = pol(x1,n=.1) # polarizer 1 with light coming in at a clockwise direction
    accw = pol(-x1,n=.1) # polarizer 1 with light coming in at a counterclockwise direction
    ccw = pol(x3,n=.1) # polarizer 3 with light coming in at a clockwise direction
    cccw = pol(-x3,n=.1) # polarizer 3 with light coming in at a counterclockwise direction
    d = pol(x4,n=0) # perfect polarizer between exiting light and detector
    DI = [] # darkport intensity
    x2s = np.arange(thetamin,thetamax,.1) # making an array of all the different rotation angles of polarizer between set max and min angles

    for x2 in x2s: 
        "iterating over all the different angles to get insentities at that set angle and putting the intensities into a list"
        bcw = pol(x2,n=.1) # polarizer 2 with light coming in at a clockwise direction
        bccw = pol(-x2,n=.1) # polarizer 2 with light coming in at a counterclockwise direction
        A = ((cccw@ bccw@ accw -acw@ bcw@ ccw)/2)
        B = ((accw@ bccw@ cccw-ccw@ bcw@ acw)/2)
        C = (L@(A)@ d@ (B)@ L) # matrix multiplacation to get intensity coming out
        DI.append(C)

    return(x2s,np.array(DI))

def IB(x1,x3,x4,thetamin = 135, thetamax = 145):
    "gives the intensity going to the bright port"
    L = np.array([1,0])
    acw = pol(x1,n=.1)
    accw = pol(-x1,n=.1)
    ccw = pol(x3,n=.1)
    cccw = pol(-x3,n=.1)
    d = pol(x4,n=0)
    BI = []
    x2s = np.arange(thetamin,thetamax,.1)

    for x2 in x2s:
        bcw = pol(x2,n=.1)
        bccw = pol(-x2,n=.1)
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
    "bright port minus dark ratio to total initial intensity"

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






