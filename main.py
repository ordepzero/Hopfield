# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 03:10:47 2016

@author: PeDeNRiQue
"""

import numpy as np
import random

def read_file(filename):
    array = []
    
    with open(filename,"r") as f:
        content = f.readlines()
        for line in content: # read rest of lines
            array.append([x for x in line.split(",")])   
    return np.array(array);
    
    
def convert_to_ones(chars):
    #print(chars)
    
    number = []
    
    for char in chars:
        if(char == "x"):
            number.append(1)
        else:
            number.append(-1)
    return number
    
def convert_to_letter(pattern):
    
    for i in range(10):
        for j in range(10):
            if(pattern[10*i+j] == 1):
                print("x",end="")
            else:
                print(".",end="")
        print()
    
def inicializate_weight_matrix(patterns):
    size = len(patterns[0])
    matrix = [[0 for x in range(size)] for y in range(size)]     
    
    for p in patterns:
        for i in range(size):
            for j in range(size):
                matrix[i][j] = matrix[i][j] + (p[i] * p[j])
                
    for i in range(size):          
        matrix[i][i] = 0
        for j in range(size):
            matrix[i][j] = matrix[i][j] / len(patterns)
            
    return matrix
    
def insert_noise(pattern):
    for i in range(len(pattern)):
        
        rand = random.randint(0, 100)
        if(rand <= 5):
            pattern[i] *= (-1)
    return pattern
    
    
def calculate_output(pattern,matrix):
    for _ in range(5):
        new_pattern = []    
        for i in range(len(pattern)):
            total = 0
            for j in range(len(matrix[i])):
                total += pattern[j] * matrix[i][j]
            if(total >= 0):
                total = 1
            else:
                total = -1
            new_pattern.append(total)
        pattern = new_pattern
    return new_pattern
    
    
if __name__ == "__main__":
    
    filename = "numbers2.txt"
        
    data = read_file(filename)    
    #print(data)
    full_number = ""
    all_numbers = []    
    
    for d in data:
        #print(d)
        
        if(len(d[0]) - d[0].count(' ') > 1):
            full_number += d[0][:10]
        else:
            all_numbers.append(full_number)
            full_number = ""
    
    
    
    print(len(all_numbers))    
    
    patterns = [convert_to_ones(chars) for chars in all_numbers]
    print(len(patterns))
    matrix = inicializate_weight_matrix(patterns)
    #print(matrix)
    
    #convert_to_letter(patterns[0])
    
    p = insert_noise(patterns[4])
    convert_to_letter(p)
    result = calculate_output(p,matrix)
    convert_to_letter(result)
    
    
    
    
    
    
    
    