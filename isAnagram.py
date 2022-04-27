# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:31:20 2022

@author: hmdebern
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s)!=len(t)):
            return False
        
        s=list(s)
        s.sort()
        
        t=list(t)
        t.sort()
        
        return  s==t
        

sol=Solution()

s="rat"
t="car"


print(sol.isAnagram(s, t))
