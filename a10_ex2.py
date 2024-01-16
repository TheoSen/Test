# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:16:26 2024

@author: TheoS
"""
import numpy as np

# todo
# applies the given function <f> for each element in the 
# given numpy array arr having any number of dimensions

# transforms the input array <arr> in place by updating 
# the results of <f> for each element directly into <arr>

# assume that the data type of elements in <arr> is 
# compatible with the function <f>

def elements_wise(arr: np.ndarray, f):
    # Iterating over arrays
    # with np.nditer(arr, op_flags = ['readwrite']) as it:
    #     for x in it:
    #         x[...] = f(x)
    # return arr
    
    # flattened <arr> to 1d array
    new_array = np.ravel(arr)
    # print(np.shares_memory(arr,new_array))
    # iterating 
    for e in range(new_array.shape[0]):
        new_array[e] = f(new_array[e])
    # reshape <arr> into the according shape
    np.reshape(new_array, np.shape(arr))    
    return new_array
            