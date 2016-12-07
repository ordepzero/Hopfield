# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 04:59:37 2016

@author: PeDeNRiQue
"""

import numpy as np

A = """
.XXX.
X...X
XXXXX
X...X
X...X
"""

_A = """
.XXX.
X...X
X.X..
....X
X...X
"""
 
Z = """
XXXXX
...X.
..X..
.X...
XXXXX
"""

def to_pattern(letter):
    from numpy import array
    return array([+1 if c=='X' else -1 for c in letter.replace('\n','')])
    
def display(pattern):
    from pylab import imshow, cm, show
    imshow(pattern.reshape((5,5)),cmap=cm.binary, interpolation='nearest')
    show()

def train(patterns):
    from numpy import zeros, outer, diag_indices 
    #r,c = patterns.shape
    r = 2
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
    

    
    
if __name__ == "__main__":
    
    patterns = [to_pattern(A),to_pattern(Z)]
    #print(len(patterns[0]))
    W = train(patterns)

    _patterns = [to_pattern(_A)]

    patterns = recall(W,_patterns)
    
    [display(p) for p in patterns]
