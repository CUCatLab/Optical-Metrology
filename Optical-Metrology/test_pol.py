import numpy as np
import nose.tools
import numpy.testing
import optical_elements as oe

def test_pol():
    "this tests that the polarization function outputs the proper polarization with different amounts of leakage"
    
    pol = oe.pol(.1)
    y = np.array([[.9949874371, 0],[0, .1]]) 
    np.testing.assert_allclose(pol,y,atol = 1e-7)
    