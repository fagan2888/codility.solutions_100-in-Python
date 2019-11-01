#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:59:33 2019

@author: jcunanan
"""
#import numpy as np

# Binary gap problem
# Find longest sequence of zeros in binary representation of an integer.

def get_one(S: str):
    new = []
    for i in range(len(S)):
       if S[i]== '1':
           new.append(i)
    return new
       
          
def solution(N: int):
    
    if type(N) != int:
        raise TypeError(str(N)+' is not an interger!')
    
    bN = "{0:b}".format(N)
    index_1 = get_one(bN)
    dist = []
    
    if index_1 == [0]:
        return 0
    else:
        
        for i in range(len(index_1)):
            if i == 1:
                dist.append(index_1[1]-index_1[0]-1)
            
            if i > 1:
                dist.append(index_1[i]-index_1[i-1]-1)
                
    return max(dist)
       
