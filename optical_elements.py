import numpy as np

# Half Waveplate function

def hwp(x1): # make all hwp functions lower case (only classer are upper case)
    "function of a half wave plate,x = rotation angle of HWP"
    hwp = np.array(([np.cos(np.deg2rad(2*x1)), 2*np.cos(np.deg2rad(x1))*np.sin(np.deg2rad(x1))], [2*np.cos(np.deg2rad(x1))*np.sin(np.deg2rad(x1)), np.sin(np.deg2rad(x1))**2 - np.cos(np.deg2rad(x1))**2])) #half waveplate matrix

    return(hwp)
# make into sanwhitch form in the same way as rm compair to above

def pol(n=.1):
    "polarizer with leakage"
    hp = np.array([[np.sqrt(1-n**2), 0],[0, n]]) #polarizer
    return(hp)

def rm(x1,n=.1):
    "polarizer on rotation mount"
    r = np.array([[np.cos(np.deg2rad(x1)),-np.sin(np.deg2rad(x1))],[np.sin(np.deg2rad(x1)),np.cos(np.deg2rad(x1))]])
    p = pol(n=n)
    rt = r.transpose()
    return(r @ p @ rt)

