# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from neupy import algorithms
from neupy import environment

environment.reproducible()

zero = np.matrix([
     0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 1, 1, 1, 0
 ])

one = np.matrix([
     0, 1, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0,
     0, 0, 1, 0, 0
 ])

two = np.matrix([
     1, 1, 1, 0, 0,
     0, 0, 0, 1, 0,
     0, 0, 0, 1, 0,
     0, 1, 1, 0, 0,
     1, 0, 0, 0, 0,
     1, 1, 1, 1, 1,
 ])
 
half_zero = np.matrix([
     0, 1, 1, 1, 0,
     1, 0, 0, 0, 1,
     1, 0, 0, 0, 1,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
 ])
 
half_two = np.matrix([
     1, 1, 1, 0, 0,
     0, 0, 0, 1, 0,
     0, 0, 0, 1, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
     0, 0, 0, 0, 0,
 ])

def draw_bin_image(image_matrix):
     for row in image_matrix.tolist():
         print('| ' + ' '.join(' *'[val] for val in row))


if __name__ == "__main__":
    
    
    data = np.concatenate([zero,one,two], axis=0)
    dhnet = algorithms.DiscreteHopfieldNetwork(mode='async')
    dhnet.n_times = 400
    dhnet.train(data)
    
    result = dhnet.predict(half_two)
    draw_bin_image(result.reshape((6, 5)))


