import numpy as np
import nose.tools
import numpy.testing
import optical_elements as oe

def test_rm():
    " this tests the the function for a polarizer on a rotation mount gives the proper output given the polarizer has a leckage of .1 and rotated at 90 degrees"
    
    rm = oe.rm(90 , .1)
    y = np.array([[.1 , 0],[0 , .9949874371]]) 
    
    np.testing.assert_allclose(rm,y,atol = 1e-7)
    
    