# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:36:38 2022

@author: hmdebern
"""


freinds=[{'name':'bob', "location":(5,2,10)},
         {'name':'da', "location":(2,3,5)},
         {'name':'ma', "location":(19,3,4)},
         {'name':'sk', "location":(3,5,1)}]


def computedis(a , b):    
    a= [ int(i) for i in a]
    b= [ int(i) for i in b] 
    
    return ( (a[0]-b[0])**2  + (a[1]-b[1])**2  + (a[2]-b[2])**2   )**0.5
    
min_val=1E9
min_person=""

distances=[]
for i in range(len(freinds)-1):
    temp=[]
    for j in range(i,len(freinds)):
        dist= computedis(freinds[i]["location"],freinds[j]["location"])
        temp.append((dist))
    distances.append(temp)
    
    sum_val=sum(temp)
    if(i!=0):
        for k in range(i):
            sum_val+=distances[k][i]
            
    if( sum_val< min_val):
        min_val= sum_val
        min_person=freinds[i]["name"]
        