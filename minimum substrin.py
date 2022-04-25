# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:43:46 2022

@author: hmdebern
"""


def solution(S):
    # write your code in Python 3.6
    substrings= dict()
    window= [x for x in range(1,len(S))]

    for w in window:
        j=0
        while j < len(S)-w+1:
            ss= S[j: j + w]
            if(ss in substrings.keys()):
                substrings[ss]+=1
            else:
                substrings[ss]=1
            j=j+1

    sorted_ss= sorted(substrings,key=substrings.get)

    sorted_ss_dict= dict()
    temp_key=[]
    for key in sorted_ss:
        if(substrings[key]==1):
                    sorted_ss_dict[key]=substrings[key]
                    temp_key.append(key)
    
    return len(temp_key[0])

t=solution('zyzyzyz')