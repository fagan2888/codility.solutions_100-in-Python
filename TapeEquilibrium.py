#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:19:46 2019

@author: jcunanan
"""
from itertools import accumulate

def solution(A):
    # write your code in Python 3.6
    L = list(accumulate(A))

    return min([abs(2 * x - L[-1]) for x in L[:-1]])
    
    
########################   53% score codes 100% correct but O(n^2) complexity
 
 #    N=len(A)
#    p_sum = [sum(A[0:i]) for i in range(1,N+1)]
#    
#    return min([abs(2 * x - p_sum[-1]) for x in p_sum[:-1]])
 
 ##########################
#    if len(A)==2:
#        return abs(A[0]-A[1])
#    
#    N=len(A)
#    p_sum = [sum(A[0:i]) for i in range(1,N+1)]
#    
#    diff = abs(2*p_sum[0]-p_sum[-1])
#    
#    for j in range(1,N-1):
#        if diff < abs(2*p_sum[j]-p_sum[-1]):
#            diff = diff
#        else:
#            diff =  abs(2*p_sum[j]-p_sum[-1])
#            
#    return diff
    

############################
    
#    diff = abs(A[0]-sum(A[1:]))
#    for i in range(2,len(A)):
#        if diff < abs(sum(A[0:i]) - sum(A[i:]) ):
#            diff = diff
#        else:
#            diff = abs(sum(A[0:i]) - sum(A[i:]) )
#            
#    return diff
#