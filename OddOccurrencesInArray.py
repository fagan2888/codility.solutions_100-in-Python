#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:39:19 2019

@author: jcunanan
"""



def solution(A):
    
    if len(A) //2 == 1:
       raise ValueError('String needs to be odd length array')
    
    no_pair = {}
    
    for num in A:
       if num in no_pair.keys():
          del no_pair[num]
       else:
           no_pair[num]=num
           

    for i in no_pair:
        odd = no_pair[i]
    
    return odd

