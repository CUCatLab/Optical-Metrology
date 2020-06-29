import numpy as np
import nose.tools
import numpy.testing # look at documentation look at what they do!!!!!!!!!!!!!!! (shows how to test on arrays)
import interferometer as ir


# define function inputs above if use more than once otherwise jusr input number in function

# turn xs into thetas for angles (tupples)

# end to end test ( should make more test funcs for smaller comps before end to end test allows you to zero in)



def test_intensity90(): # shouldnt have arguement
    " functon to test the intesity function in the interferometer module"
    xs,Is = ir.intensity(10, -40, 90, 0, 180) # choose arguments that are easy to compute and that you know the answer to  
    # use simplist angles that give the most obvious answers and 1 less obvious test
    assert np.all(Is >= 0) # returns new numpy array of all booleans then outputs a single boolean passed to assert func if true does nothing if false raises an exception
    
    # find sci comp book and refamiliarize
    
    # if testing floats equality use aproxmatly equal (gives error bars) safer cuz doesnt round
    # open terminal and type nose to run
    
    
def test_intensity0(): # shouldnt have arguement
    " functon to test the intesity function in the interferometer module"
    xs,Is = ir.intensity(10, -40, 0, 0, 180) 
    
    assert np.all(Is >= 0)
    
def test_intensity45(): # shouldnt have arguement
    " functon to test the intesity function in the interferometer module"
    xs,Is = ir.intensity(10, -40, 45, 0, 180) 
    
    assert np.all(Is >= 0)