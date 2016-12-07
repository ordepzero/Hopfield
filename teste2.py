# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 04:59:37 2016

@author: PeDeNRiQue
"""

import numpy as np

A = """
xxxxx
...xx
xxxxx
...xx
xxxxx
"""

_A = """
xxxxx
...xx
xxxxx
...xx
xxxxx
"""
 
Z = """
xxxxx
...x.
..x..
.x...
xxxxx
"""

def read_file(filename):
    array = []
    
    with open(filename,"r") as f:
        content = f.readlines()
        for line in content: # read rest of lines
            array.append([x for x in line.split(",")])   
    return np.array(array);

def to_pattern(letter):
    from numpy import array
    return array([+1 if c=='x' else -1 for c in letter.replace('\n','')])
    
def display(pattern):
    from pylab import imshow, cm, show
    imshow(pattern.reshape((5,5)),cmap=cm.binary, interpolation='nearest')
    show()

def train(patterns):
    from numpy import zeros, outer, diag_indices 
    #r,c = patterns.shape
    r = 10
    c = 25
    W = zeros((c,c))
    for p in patterns:
        W = W + outer(p,p)
    W[diag_indices(c)] = 0
    print(W)
    return W/r
    
def recall(W, patterns, steps=5):
    from numpy import vectorize, dot
    sgn = vectorize(lambda x: -1 if x<0 else 1)
    for _ in range(steps):        
        patterns = sgn(dot(patterns,W))
    return patterns   
    
def convert_to_ones(chars):
    #print(chars)
    
    number = []
    
    for char in chars:
        if(char == "x"):
            number.append(1)
        else:
            number.append(-1)
    return number
    
    
if __name__ == "__main__":
    
    filename = "numbers.txt"
        
    data = read_file(filename)    
    #print(data)
    full_number = ""
    all_numbers = []    
    
    for d in data:
        #print(d)
        
        if(len(d[0]) - d[0].count(' ') > 1):
            full_number += d[0][:5]
        else:
            all_numbers.append(full_number)
            full_number = ""
    
    patterns = [convert_to_ones(chars) for chars in all_numbers]
    #print(len(patterns[0]))
    W = train(patterns)

    _patterns = [to_pattern(_A)]

    patterns = recall(W,_patterns)
    
    [display(p) for p in patterns]
