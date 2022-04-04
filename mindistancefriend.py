# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:04:24 2022

@author: hmdebern
"""



lists=[[1,4,5],[1,3,4],[2,6]]


ans =lists[0]
for i in range( 1, len(lists)):
    temp= lists[i]
    for item in temp:
        ans.append(item)

ans.sort()


    
    


