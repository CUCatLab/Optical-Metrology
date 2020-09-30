import numpy as np
import nose.tools
import numpy.testing # look at documentation look at what they do!!!!!!!!!!!!!!! (shows how to test on arrays)
import optical_elements as oe

def test_HWP0():
    "this test funtion test that the half waveplate function gives the correct output when at a 0 degree angle"
    
    hwp = oe.hwp(0)
    y = np.array(([1, 0], [0, -1]))
    
    np.testing.assert_allclose(hwp,y,atol = 1e-7)
    
def test_HWP90():
    "this test funtion test that the half waveplate function gives the correct output when at a 90 degree angle"
    
    hwp = oe.hwp(90)
    y = np.array(([-1, 0], [0, 1]))
    
    np.testing.assert_allclose(hwp,y,atol = 1e-7)
    
    
    