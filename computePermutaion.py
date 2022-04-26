# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:08:26 2022

@author: hmdebern
"""



def computePermutaion(lst):
    
    if(len(lst)==0):
        return []
    elif(len(lst)==1):
        return [lst]
    else:
        output=[]
        for i in range(len(lst)):
            current_item= lst[i]
            remaining_items= lst[: i] + lst[i+1:]
            
            for k in computePermutaion(remaining_items):
                temp=[current_item]+k
                if(temp not in output):
                    output.append(temp)
    return output


 
print(computePermutaion(['a','b','c'])) 
