import numpy as np
import optical_elements as oe
import matplotlib.pyplot as plt

### pretense with oe

def intensity(x1,x3,x4,x2min, x2max,l= np.array([1,0]), x1error = 0.0, x3error = 0.0, aeff = 0.1, beff = .1, ceff = .1, deff = 0.0):
    
    """Function docstring, one line summary
    All functions should have their own documentation via docstrings.
    Function arguments are positional, unless they are provided a default
    value to become a "keyword argument".
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.
    The function doc string should describe the name of the function,
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.
    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
    All indentation should be 4 spaces.  NO TABS IN PYTHON CODE.
    Parameters
    ----------
        arg1 : type
            Describe the arguments of the function
        x1 : integer
            this is the rotation angle of the 1st half wave plate
        x3 : integer
            this is the rotation angle of the 2nd half wave plate
        x4 : integer
            angle of rotation for the polarizer between exiting light and detector
         x2min : float
             minimum angle for the middle imperfect polarizer
         x2max : float
             maximum angle for the middle imperfect polarizer
        
        kwarg1: type (default: value), optional
            Describe keyword arguments of function
        x1error : float
            human error for x1 angle
        x3error : float
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
            Describe the type and content of what the function returns here.
            It can be useful to give an example if the type is complicated.
    Raises
    ------
        If any exceptions can be raised by the function, describe them."""
    
    #make a function that spits out whatever your lights going to be depending on polarization (nothing should be set since we can 
    "gives the intensity going to the dark port"
     # l = laser light going into interferometer horizonatlly polarized
    acw = oe.hwp(-x1) @ oe.pol(n=aeff) @ oe.hwp(x1+x1error) # polarizer 1 with light coming in at a clockwise direction ( HWP @ pol@ )make sure both HWP can have dif angles
    accw = oe.hwp(x1+x1error) @ oe.pol(n=aeff) @ oe.hwp(-x1) # polarizer 1 with light coming in at a counterclockwise direction
    ccw = oe.hwp(-x3) @ oe.pol(n=ceff) @ oe.hwp(x3+x3error) # polarizer 3 with light coming in at a clockwise direction
    cccw = oe.hwp(x3+x3error) @ oe.pol(n=ceff) @ oe.hwp(-x3) # polarizer 3 with light coming in at a counterclockwise direction
    d = oe.rm(x4,n= deff) # perfect polarizer between exiting light and detector
    # leave a space here because x2s defining array and above variables defining matrices
    x2s = np.arange(x2min,x2max,.1) # making an array of all the different rotation angles of polarizer between set max and min angles

    @np.vectorize # even though give and return one value its going to take finc and make it work on an array of values
    def darkport_intensity(x2):
        
        bcw = oe.rm(x2,n=beff) # polarizer 2 with light coming in at a clockwise direction
        bccw = oe.rm(-x2,n=beff) # polarizer 2 with light coming in at a counterclockwise direction
        b = ((accw@ bccw@ cccw-ccw@ bcw@ acw)/2)
        a = b.transpose()
        c = (l@(a) @d @ (b)@ l)
        return (c)
    
    
    return(x2s,darkport_intensity(x2s))


def vertical(x1,x3,x2min, x2max):
    "this plots the the vertical light coming out of the dark port"
    x2s,Vt = intensity(x1,x3,90,x2min, x2max)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Vt,color="purple")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$I_b/I_0$')
    plt.title('Vertical Dark Port Intensity vs Polarizer Angle')
    plt.grid(True)
    plt.xlim((x2min,x2max))
    plt.show()
    return(f)

def horizontal(x1,x3,x2min, x2max ):
    "this plots the horizontal light coming out of the darkport"
    x2s,Hz = intensity(x1,x3,0, x2min, x2max)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,Hz,color="magenta")
    plt.xlabel(r"$\phi$ (deg)")
    plt.ylabel(r"$I_d/I_0$")
    plt.title("Horizontal Dark Port Intensity vs Polarizer Angle")
    plt.grid(True)
    plt.xlim((x2min,x2max))
    plt.show()
    return(f)

def split(x1,x3,x2min, x2max):
    "bright port minus dark ratio to total initial intensity"

    x2s,Vt = intensity(x1,x3,90,x2min, x2max)
    x2s,Hz = intensity(x1,x3,0,x2min, x2max)
    s = Vt-Hz / (Hz+Vt)
    f=plt.figure(figsize=(4,3))

    plt.plot(x2s,s,color="aqua")
    plt.xlabel(r'$\phi$ (deg)')
    plt.ylabel(r'$(I_v-I_h)/(I_h+I_v)$')
    plt.title('Dark Port Intensity Difference')
    plt.xlim((x2min,x2max))
    plt.grid(True)
    plt.show()
    return(f)