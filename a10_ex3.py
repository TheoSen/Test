# todo
# write a function that performs one-hot-encoding for each element
# in the input 1D array <arr>, and the returned result is a numpy
# 2D array in which i_th row is the encoding of the i_th element in arr.

import numpy as np

def one_hot_encoding(arr: np.ndarray) -> np.ndarray:

    # condition check
    # check <arr> is 1D array
    if arr.ndim != 1:
        raise ValueError(f'The function can work for 1D matrices, not {arr.ndim}D')
    
    # creat empty array according to the size of <arr>
    encoded_array = np.empty(shape=(0,arr.shape[0]))


    # one-hot-encoding

    # sort the unique value
    ## creat the reference array
    ref_array = np.sort(arr)
    
    # print(f'reference : {ref_array}')

    
    for elem in ref_array:
        # get the encoding array with np.where and stack on top of each other (row wise).
        encoded_array = np.vstack((encoded_array,np.where(arr==elem, 1, 0)))
    
    return encoded_array


