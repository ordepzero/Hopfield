# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 06:29:04 2016

@author: PeDeNRiQue
"""

import numpy as np
import random
from numpy import vectorize, dot
from pylab import imshow, cm, show



def read_file(filename):
    array = []
    
    with open(filename,"r") as f:
        content = f.readlines()
        for line in content: # read rest of lines
            array.append([x for x in line.split(",")])   
    return np.array(array);
    
def convert_to_ones(chars):
    
    number = []
    
    for char in chars:
        if(char == "x"):
            number.append(1)
        else:
            number.append(-1)
    return number
    
def convert_to_number(pattern):
    
    for i in range(10):
        for j in range(10):
            if(pattern[10*i+j] == 1):
                print("x",end="")
            else:
                print(".",end="")
        print()
        
def insert_noise(pattern):
    for i in range(len(pattern)):
        
        rand = random.randint(0, 100)
        if(rand <= 20):
            pattern[i] *= (-1)
    return pattern
    
def display(pattern):
    imshow(pattern.reshape((10,10)),cmap=cm.binary, interpolation='nearest')
    show()

def inicializate_weight_matrix(patterns):
    size = len(patterns[0])
    matrix = [[0 for x in range(size)] for y in range(size)]     
    
    #print(len(matrix),len(matrix[0]),len(patterns),len(patterns[0]))    
    
    for p in patterns:
        for i in range(size):
            for j in range(size):
                matrix[i][j] = matrix[i][j] + (p[i] * p[j])
                
    for i in range(size):          
        matrix[i][i] = 0
        for j in range(size):
            matrix[i][j] = matrix[i][j] / len(patterns)
    return matrix
    
def recall(W, patterns, steps=40):
    sgn = vectorize(lambda x: -1 if x<0 else 1)
    for _ in range(steps):        
        patterns = sgn(dot(patterns,W))
    return patterns   
    
if __name__ == "__main__":
    
    filename = "numbers2.txt"
        
    data = read_file(filename)    
    #print(len(data))
    full_number = ""
    all_numbers = []    
    
    for d in data:
        #print(d)
        
        if(len(d[0]) - d[0].count(' ') > 1):
            full_number += d[0][:10]
        else:
            all_numbers.append(full_number)
            full_number = ""
    
    numbers = [convert_to_ones(chars) for chars in all_numbers]
    
    #[convert_to_number(p) for p in numbers]
    
    matrix = inicializate_weight_matrix(numbers)
    
    noisy_number = insert_noise(numbers[0])
    
    convert_to_number(noisy_number)
    patterns = recall(matrix,noisy_number)
    convert_to_number(patterns)    
    
    '''

    patterns = recall(W,_patterns)
    
    [display(p) for p in patterns]
    '''
