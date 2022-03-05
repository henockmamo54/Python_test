# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:35:03 2022

@author: hmdebern
"""

# def square(x):
#     return x*x

import itertools

def computeValue(values,m):
    
    modulo_values=[]
   
    for element in itertools.product(*values):  
        temp = sum([x**2 for x in element])%m
        modulo_values.append(temp) 
        
    return max(modulo_values)

    

values=[[1,2,3],
       [1,2,3]]

print(computeValue(values, 5))


# if __name__=='__main__':
#     print('__main__')
    
#     input_values=[]
    
    
#     k,m=[int(x) for x in input().split(' ')]
#     for i in range(k):
#         input_values.append(input().split(' '))
        
#     computeValue(input_values,m)
    



    
# from itertools import product

# K,M = map(int,input().split())
# N = (list(map(int, input().split()))[1:] for _ in range(K))
# results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
# print(max(results))

