# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:51:29 2022

@author: hmdebern
"""



arr=[[-9,-9,-9,1,1,1],
[0,-9,0,4,3,2],
[-9,-9,-9,1,2,3],
[0,0,8,6,6,0],
[0,0,0,-2,0,0],
[0,0,1,2,4,0]]

g=[[1,1,1],[0,1,0],[1,1,1]]


h=0
w=0
temp_vals=[]

while(h+2<6):
    w=0
    while(w+2<6):
        # a_s=arr[h:h+3][w:w+3]
        temp_sum= sum(arr[h][w:w+3]) 
        temp_sum+= arr[h+1][w+1]
        temp_sum += sum(arr[h+2][w:w+3]) 
        
        
        temp_vals.append( temp_sum )
             
        w+=1
    h+=1
    
    
print(max(temp_vals))