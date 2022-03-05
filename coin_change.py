# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 15:41:07 2022

@author: hmdebern
"""
 

def coin_change(N,coin_list):    
    ways=[list(range(0,N+1))]     
    for i in range(1,len(coin_list)):
        temp=[]    
        for j in range(N+1):        
            if(j-coin_list[i]>=0):             
                temp.append(min(ways[i-1][j],   temp[j-coin_list[i]]+1))            
            else:
                temp.append(ways[i-1][j])                 
        ways.append((temp))        
    return ways[-1][N]


  
def coin_change2(N,coin_list):  
    ways=list(range(0,N+1))     
    for i in range(1,len(coin_list)):
        for j in range(coin_list[i],N+1): 
            ways[j]=(min(ways[j],   ways[j-coin_list[i]]+1))             
    return ways[N]
                
def coin_change3(N,coin_list): 
    ways= [1E6]*(N+1)
    ways[0]=0
    for i in coin_list:
        for j in range(N+1):    
            if(j-i>=0):
                ways[j]= (min(ways[j],   ways[j-i]+1))   
    if ways[N]==1E6:
        return -1
    else:
        return ways[N]

coin_list = [1,5,10]
N = 12

print(coin_change(N,coin_list))
print(coin_change2(N,coin_list))
print(coin_change3(N,coin_list)) 

print('=================================')
coin_list = [2]
N = 3

print(coin_change(N,coin_list))
print(coin_change2(N,coin_list))
print(coin_change3(N,coin_list)) 


        

        
