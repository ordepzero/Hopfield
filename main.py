# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 03:10:47 2016

@author: PeDeNRiQue
"""

import numpy as np

def read_file(filename):
    array = []
    
    with open(filename,"r") as f:
        content = f.readlines()
        for line in content: # read rest of lines
            array.append([x for x in line.split(",")])   
    return np.array(array);
    
    
def convert_to_ones(chars):
    print(chars)
    
    number = []
    
    for char in chars:
        if(char == "x"):
            number.append(1)
        else:
            number.append(-1)
    return number

def inicializate_weight_matrix(patterns):
    size = len(patterns[0])
    matrix = [[0 for x in range(size)] for y in range(size)]     
    
    for p in patterns:
        for i in range(size):
            for j in range(size):
                matrix[i][j] = matrix[i][j] + (p[i] * p[j])
    
    return matrix 
    

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
    #print(patterns)
    matrix = inicializate_weight_matrix(patterns)
    print(matrix)
    
    
    
    
    
    
    
    
    
    
    
    
    