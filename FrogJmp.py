#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 01:23:05 2019

@author: jcunanan
"""

import math

def solution(X, Y, D):
    # write your code in Python 3.6
    T = (Y-X)/D
    jump = math.ceil(T)
    
    return jump