import numpy as np
import optical_elements as oe
import matplotlib.pyplot as plt

### pretense with oe

def intensity(theta1,theta3,theta4,theta2min, theta2max,l= np.array([1,0]), theta1error = 0.0, theta3error = 0.0, aeff = 0.1, beff = .1, ceff = .1, deff = 0.0):
    
    """
    the intensity function represents how the intensity of the laser light changes as it goes through the interferometer set up.
     
    Parameters
    ----------
        theta1 : integer
            this is the rotation angle of the 1st half wave plate
        theta3 : integer
            this is the rotation angle of the 2nd half wave plate
        theta4 : integer
            angle of rotation for the polarizer between exiting light and detector
         theta2min : float
             minimum angle for the middle imperfect polarizer
         theta2max : float
             maximum angle for the middle imperfect polarizer
        
        theta1error : float
            human error for x1 angle
        theta3error : float
            human error for x2 angle
         aeff : float
             polarization leakage for 1st half waveplate polarizer set up
         beff : float
             polarization leakage for middle polarizer
         ceff : float
             polarization leakage for 2nd half waveplate polarizer set up
         deff : float
             polarization leakage for the polarizer inbetween the interferometer set up and the detector
    Returns
    -------
        type :
            the return value should be a range of intensities that are a result of the final intensity coming out of the set up
            with different polarization angles.
    """
    
    #make a function that spits out whatever your lights going to be depending on polarization (nothing should be set since we can 
    "gives the intensity going to the dark port"
     # l = laser light going into interferometer horizonatlly polarized
    acw = oe.hwp(-theta1) @ oe.pol(n=aeff) @ oe.hwp(theta1+theta1error) # polarizer 1 with light coming in at a clockwise direction ( HWP @ pol@ )make sure both HWP can have dif angles
    accw = oe.hwp(theta1+theta1error) @ oe.pol(n=aeff) @ oe.hwp(-theta1) # polarizer 1 with light coming in at a counterclockwise direction
    ccw = oe.hwp(-theta3) @ oe.pol(n=ceff) @ oe.hwp(theta3+theta3error) # polarizer 3 with light coming in at a clockwise direction
    cccw = oe.hwp(theta3+theta3error) @ oe.pol(n=ceff) @ oe.hwp(-theta3) # polarizer 3 with light coming in at a counterclockwise direction
    d = oe.rm(theta4,n= deff) # perfect polarizer between exiting light and detector
    # leave a space here because x2s defining array and above variables defining matrices
    theta2s = np.arange(theta2min,theta2max,.1) # making an array of all the different rotation angles of polarizer between set max and min angles

    @np.vectorize # even though give and return one value its going to take finc and make it work on an array of values
    def darkport_intensity(theta2):
        ""
        
        bcw = oe.rm(theta2,n=beff) # polarizer 2 with light coming in at a clockwise direction
        bccw = oe.rm(-theta2,n=beff) # polarizer 2 with light coming in at a counterclockwise direction
        b = ((accw@ bccw@ cccw-ccw@ bcw@ acw)/2)
        a = b.transpose()
        c = (l@(a) @d @ (b)@ l)
        return (c)
    
    
    return(theta2s,darkport_intensity(theta2s))


def vertical(theta1,theta3,theta2min, theta2max,ymax=0.2,n=.1):
    "this plots the the vertical light coming out of the dark port"
    x2s,Vt = intensity(theta1,theta3,90,theta2min, theta2max)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Vt,color="purple")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$I_b/I_0$')
    plt.title('Vertical Dark Port Intensity vs Polarizer Angle')
    plt.grid(True)
    plt.xlim((theta2min,theta2max))
    plt.ylim((0,ymax))
    plt.show()
    



def horizontal(theta1,theta3,theta2min, theta2max, ymax=0.2,n=.1 ):
    "this plots the horizontal light coming out of the darkport"
    x2s,Hz = intensity(theta1,theta3,0, theta2min, theta2max)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Hz,color="magenta")
    plt.xlabel(r"$\phi$ (deg)")
    plt.ylabel(r"$I_d/I_0$")
    plt.title("Horizontal Dark Port Intensity vs Polarizer Angle")
    plt.grid(True)
    plt.xlim((theta2min,theta2max))
    plt.ylim((0,ymax))
    plt.show()



def split(theta1,theta3,theta2min, theta2max,n=.1):
    "bright port minus dark ratio to total initial intensity"

    x2s,Vt = intensity(theta1,theta3,90,theta2min, theta2max)
    x2s,Hz = intensity(theta1,theta3,0,theta2min, theta2max)
    s = Vt-Hz / (Hz+Vt)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,s,color="aqua")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$(I_v-I_h)/(I_h+I_v)$')
    plt.title('Dark Port Intensity Difference')
    plt.xlim((theta2min,theta2max))
    plt.grid(True)
    plt.show()