# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:21:46 2022

@author: hmdebern
"""



nums1 = [1,2]
nums2 = [3,4]


nums12=[] 
itteration_item=[]
if(len(nums1)>len(nums2)):
    nums12=nums1
    itteration_item= (nums2)
else:
    nums12=nums2
    itteration_item= (nums1)
    

for i in (itteration_item):
    nums12.append(i)
    
    
nums12.sort()

if(len(nums12)%2==0):
     
    index = (int)(len(nums12)/2)
    val= (nums12[index]+ nums12[index -1 ])/2
    print(val)
else:
    index= (int)(len(nums12)/2)
    val = nums12[index]
    print(val)
    
