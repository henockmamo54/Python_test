# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:49:52 2022

@author: hmdebern
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        output=set()             
        for n in nums:            
            if(n in output):
                return True
            output.add(n)
            
        return False