# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:10:29 2022

@author: hmdebern
"""




import math 


# # # AB= int(input())
# # # BC= int(input())

AB= 100
BC= 1


AC= (AB**2 + BC**2)**0.5

print(AC)
 
c= round( math.asin( AB/AC) *180/math.pi)

print(c)

# degree_sign = u"\N{DEGREE SIGN}" 


# print(degree_sign)


# if __name__=='__main__':
    
#     AB= int(input())
#     BC= int(input())
#     AC= (AB**2 + BC**2)**0.5
#     c= round( 90 -  math.asin( AB/AC) *180/math.pi)
#     print(str(c)+'°')