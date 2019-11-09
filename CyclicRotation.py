#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:44:43 2019

@author: jcunanan
"""

def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 1 or len(A) == 0:
        return A
        
    elif len(A) < K:
        m = K%len(A)
        B = [A[i-m] for i in range(len(A))   ]
        
    else:
        B = [A[i-K] for i in range(len(A))   ]
        
    return B   