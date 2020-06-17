import numpy as np
import optical_elements as oe

### pretense with oe

def intensity(x1,x3,thetamin, thetamax, x4):
    
    #make a function that spits out whatever your lights going to be depending on polarization (nothing should be set since we can 
    "gives the intensity going to the dark port"
    L = np.array([1,0]) # laser light going into interferometer horizonatlly polarized
    acw = oe.HWP(-x1) @ oe.pol(n=.1) @ oe.HWP(x1) # polarizer 1 with light coming in at a clockwise direction ( HWP @ pol@ )make sure both HWP can have dif angles
    accw = oe.HWP(x1) @ oe.pol(n=.1) @ oe.HWP(-x1) # polarizer 1 with light coming in at a counterclockwise direction
    ccw = oe.HWP(-x3) @ oe.pol(n=.1) @ oe.HWP(x3) # polarizer 3 with light coming in at a clockwise direction
    cccw = oe.HWP(x3) @ oe.pol(n=.1) @ oe.HWP(-x3) # polarizer 3 with light coming in at a counterclockwise direction
    d = oe.rm(x4,n=0) # perfect polarizer between exiting light and detector
    DI = [] # darkport intensity
    x2s = np.arange(thetamin,thetamax,.1) # making an array of all the different rotation angles of polarizer between set max and min angles

    
    for x2 in x2s: 
        "iterating over all the different angles to get insentities at that set angle and putting the intensities into a list"
        bcw = oe.rm(x2,n=.1) # polarizer 2 with light coming in at a clockwise direction
        bccw = oe.rm(-x2,n=.1) # polarizer 2 with light coming in at a counterclockwise direction
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