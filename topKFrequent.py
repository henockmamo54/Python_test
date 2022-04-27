# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:10:32 2022

@author: hmdebern
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output=dict()
        
        for n in nums:
            
            if(n in output):
                output[n]+=1
            else:
                output[n]=1
        
        sortedvals= sorted(output.items(),key=lambda x: x[1],reverse=True)
        
        return [x[0] for x in sortedvals[:k]]