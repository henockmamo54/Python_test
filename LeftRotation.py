# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:50:53 2022

@author: hmdebern
"""


d=4
arr=[1,2,3,4,5]

def rotateLeft(d, arr):
    n=len(arr)
    ans=[0]*n
    for i in range(n): 
        ans[i-d]= arr[i]
    return ans
        
    
    
print(rotateLeft(d, arr))