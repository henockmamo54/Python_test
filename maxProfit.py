# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:59:23 2022

@author: hmdebern
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit=0
        for i in range(len(prices)):
            for j in range(len(prices)-1,i,-1):
                if(prices[i]<prices[j]):
                    max_profit=max(max_profit, prices[j]-prices[i])
        return max_profit
                
    
    def maxProfit2(self, prices: List[int]) -> int:
        
        res = 0
        
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res