# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 21:33:58 2022

@author: hmdebern
"""


class Solution:
    
    def computePermutaion(self,lst):
        
        if(len(lst)==0):
            return []
        elif(len(lst)==1):
            return [lst]
        else:
            output=[]
            for i in range(len(lst)):
                current_item= lst[i]
                remaining_items= lst[: i] + lst[i+1:]
                
                for k in self.computePermutaion(remaining_items):
                    temp=[current_item]+k
                    if(temp not in output):
                        output.append(temp)
        return output
    
    def getAllIndicis(self,string, word):
        # print(word)
        string_len=0;
        output=[]
        while(string_len<len(string)):
            try:    
                temp=string[string_len:].index(word)
                output.append(temp)
                string_len=temp+1
            except:
                break
        return output
        
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        outputs=[]
        
        # generate the concatination of words
        words_comb=self.computePermutaion(words)
        
        
        for word in words_comb: 
            try:                
                outputs.append(s.index("".join(word)))
                # print(self.getAllIndicis(s,("".join(word))))
                # outputs=outputs+ self.getAllIndicis(s,("".join(word)))
            except:
                continue
        return outputs