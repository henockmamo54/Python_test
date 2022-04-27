# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:02:51 2022

@author: hmdebern
"""

class Solution:
    def maxArea(self, height) -> int:
        
        
        max_val=0
        l=0
        r= len(height)-1
        
        
        while(l<r):            
            
            max_val=max(max_val, (r-l)*min(height[l],height[r]) )
            
            if(height[l]>=height[r]):
                r=r-1
            else:
                l=l+1
        
        return max_val 
            
    

solution= Solution()    

t=solution.maxArea([1,8,6,2,5,4,8,3,7])



