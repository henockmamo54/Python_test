# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:41:51 2022

@author: hmdebern
"""

class Solution:
    def groupAnagrams(self, strs) :
        output=dict()
        
        for word in strs:
            
            key=''.join(sorted(word))
            
            if(key in output):
                output[key].append(word)
            else:
                output[key]=[word]
        
        res=[]
        for k in output:
            res.append(output[k])
            
        return res
    
    
    
strs = ["eat","tea","tan","ate","nat","bat"]

s=Solution()
pp=s.groupAnagrams((strs))
                
            
            
                
        