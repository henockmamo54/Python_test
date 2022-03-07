# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:58:33 2022

@author: hmdebern
"""

# https://www.geeksforgeeks.org/trapping-rain-water/

height= [2,0,2]
# height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def getTotalRainWater2(height):
    l=0
    r=len(height)-1
    
    max_l=height[l]
    max_r=height[r]
    result=0
    
    
    while(l<r):
        
        if(max_l<max_r):
            l+=1
            max_l= max(max_l,height[l])
            result  += max_l-height[l]
        else:
            r-=1
            max_r = max(max_r,height[r])
            result  += max_r-height[r]
    
    return result
        
        

def getTotalRainWater(height):
    
    r=0
    n=len(height)
    
    for h in range(n):
        
        left_max  = height[h]
        right_max = height[h]
        
        for i in range(h):
            left_max= max(left_max,height[i])
        
        for i in range(h,n):
            right_max= max(right_max,height[i])
            
        r += min(left_max,right_max) - height[h]
        
    return r
   
  
print(getTotalRainWater(height))
print(getTotalRainWater2(height))



    
    
# r=0
# lower  = height[0]
# higher = height[0]

# for val in height[1:]:
    
#     if(val>=higher):
#         # r+=higher-lower
#         higher=val
#         lower=val
#     else:
#         # if(val <lower):
#         lower= val
#         r+=higher-lower  
   

# if(h<lower):
#     r+= higher-lower
#     lower=h
# elif(h>lower):
#     lower=h
#     higher=h



# if(h>0 & h>lower):
#     r+= h-lower
# elif(h<higher):
#     lower=h
#     hegher=h
    
    