#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 02:19:59 2019

@author: jcunanan
"""

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    
    S1 = sum(A)
    S2 = (N+2) * (N+1) / 2
    
    return int(S2-S1)