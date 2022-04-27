# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:38:48 2022

@author: hmdebern
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        # s=''.join([x for x in s.lower() if str.isalnum(x)])        
        # return (s==s[::-1])
        
        
        s=s.lower()        
        s=''.join([x for x in s if str.isalnum(x)])      
        
        # s=re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        
        return (s==s[::-1])
        
    def isPalindrome2(self, s: str) -> bool:
         
        
        s=s.lower()        
        s=''.join([x for x in s if str.isalnum(x)])      
        
        l=0
        r=len(s)-1
        
        while(l<r):
            
            if(s[l]!=s[r]):
                return False
            else:
                l=l+1
                r=r-1
        
        
        return True
    
    def isPalindrome3(self, s: str) -> bool:
        
        
        # s=s.lower()        
        # s=''.join([x for x in s if str.isalnum(x)])      
        
        l=0
        r=len(s)-1
        
        while(l<r):
            
            while(  not str.isalnum(s[l])  and l<r):
                l=l+1
            while( not str.isalnum(s[r]) and l<r):
                r=r-1
            
            if(s[l].lower()!=s[r].lower()):
                return False
            else:
                l=l+1
                r=r-1
        
        
        return True
        
    
        
solution= Solution()    
# print(solution.isPalindrome3("A man, a plan, a canal: Panama"))
print(solution.isPalindrome3("race a car"))