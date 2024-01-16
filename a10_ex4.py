# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 02:34:59 2024

@author: TheoS
"""
import numpy as np

def moving_average_2D(arr: np.ndarray, size: int) -> np.ndarray:
    
    # condition check
    # <arr> not 2D
    if arr.ndim !=2 :
        raise ValueError('apply for 2D array, not {arr.ndim}D')
    # elements in <arr> are not numbers 
    elif not np.issubdtype(arr.dtype, np.number):
        raise TypeError('Invalid data type')
    # size must be greater than 1 and smaller than dimension of <arr>
    elif size < 1 or size > arr.shape[0] or size > arr.shape[1] :
        raise ValueError('Invalid window size')
        
    # initializing the array
    # result is a 2D array of type float of shape(nr-size+1, nc-size+1)
    # <nr,nc> is the shape of the input array
    (nr,nc) = arr.shape
    maverage_array = np.empty(shape = (nr-size+1, nc-size+1), dtype = float)
    
    # a window of size x size starts at the upper-left corner or <arr>
    i = 0
    j = 0
    # i indicate row and j indicate col
    while(i + size <= nr):
        window_array = arr[i:size+i, j:size+j]
        # print(f'current window:\n {window_array}')
        # print(f'current mean: {np.mean(window_array)}')
        # cal the mean and save into result 
        maverage_array[i][j] = np.mean(window_array)
        j += 1
        
        # end of col reached
        if(j + size > nc):
            # reset col tracker to 0
            j = 0
            # move to next row
            i += 1
        
    return maverage_array