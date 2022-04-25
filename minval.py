# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:21:55 2022

@author: hmdebern
"""





def solution(A):
    # write your code in Python 3.6
    max_val= max(A)
    set_a=set([x for x in A if x >0])
    
    if(len(set_a)==0):
        return 1
    
    set_b= set([ x for x in range(1,max_val+2)])

    temp=list(set_b-set_a)
    if(len(temp)==0):
        return 1
    else:
        return min(temp) 
    

A= [-1, -3]

t=solution(A)