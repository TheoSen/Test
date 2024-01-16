# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:35:24 2024

@author: TheoS
"""
# getting dimension using np.ndim
# using np.shape to get rows and cols

import numpy as np
import numbers


def extend(arr: np.ndarray, rows: int, cols: int, fill = None) -> np.ndarray:
    
    # condition check
    # check dimension
    if arr.ndim != 2 :
        raise ValueError(f'can only extend 2D arrays, not {arr.ndim}D')
    # check rows:
    elif(rows < arr.shape[0]):
        raise ValueError("invalid rows")
    # check cols:
    elif(cols<arr.shape[1]):
        raise ValueError("invalid cols")
    # check fill:
    elif(fill is not None and not isinstance(fill, numbers.Number)):
        raise ValueError("invalid fill") 
        
    # do something
    
    # rows or cols could equal to the rows or cols of the arr
    # determine the new rows and cols
    
    # both row and col match with arr
    if rows == arr.shape[0] and cols == arr.shape[1]:
        new_array = arr  
        return new_array
    else:
        # creat new_array with the same type of arr
        # but the shape is set with rows and cols
        new_array = np.empty_like(arr,shape=(rows,cols))
    
    
    # write the rest of new_array
    # fill is provided
    if fill is not None:
        # filling the new_array with value<fill>
        new_array.fill(fill)
       
    # fill is not provided
    else:
        # todo
        # cal the mean of rows
        for i in range(arr.shape[0]):
            # row: starting from 0 till the row of arr 
            # cols: starting from cols of arr till end
            new_array[i:arr.shape[0],arr.shape[1]:] = np.mean(arr,axis = 1)[i]
                                        
        # cal the mean of cols
        for i in range(arr.shape[1]):
            # row: starting from row of arr till end
            # col: starting from 0 till the col of arr
            new_array[arr.shape[0]:,i:arr.shape[1]] = np.mean(arr,axis = 0)[i]
            
        # write fill into new_array
        new_array[arr.shape[0]:,arr.shape[1]:]=np.mean(arr)
        
    # write arr into new_array
    new_array[0:arr.shape[0], 0:arr.shape[1]]= arr
    
    # return the result
    return new_array