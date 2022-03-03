# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:07:24 2022

@author: hmdebern
"""

def merge_the_tools(string, k): 
    for i in range(0,len(string),k):
        temp=[] 
        [temp.append(x) for x in string[i:i+k] if x not in temp]
        print(''.join(temp))
     
     
s = 'DAABCAAAD'
 
merge_the_tools(s,3)