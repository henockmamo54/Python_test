# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:27:42 2022

@author: hmdebern
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node =ListNode()  
        last_node= node
        
        while(head!=None):
            
            temp_nodes=[]     
            
            intherange=True
            for i in range(k):
                temp_nodes.append(head)
                if(head.next is None and i!=k-1):
                    intherange=False 
                    head= None
                    break
                else:
                    head= head.next
                
            if(intherange):
                for i in range(k-1,-1,-1):                    
                    last_node.next= temp_nodes[i]
                    last_node= temp_nodes[i] 
            else:
                for temp in temp_nodes:                    
                    last_node.next= temp
                    last_node=temp
        last_node.next=None
            
        return node.next
        
        
        
s=Solution()

head=ListNode(1)

for i in range(2,3):
    node= ListNode(i)    
    temp=head
    while(temp.next):
        temp=temp.next
    temp.next= node 

# temp=head
# while(temp):
#     print(temp.val,end =" ")
#     temp=temp.next
    
output= s.reverseKGroup(head, 2)
temp=output

while(temp):
    print(temp.val,end =" ")
    temp=temp.next
    