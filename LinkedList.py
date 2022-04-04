# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:01:42 2022

@author: hmdebern
"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        new_node= Node(new_data)
        new_node.next= self.head       
        self.head=new_node
        
    def append(self,new_data):
        
        new_node= Node(new_data)
        
        if(self.head is None):
            self.head=new_node
            return
        
        last = self.head
        
        while(last.next):
            last = last.next 
            
        last.next= new_node
        
    def print(self):
        node= self.head
        while(node):
            print(node.data)
            node= node.next


l=LinkedList()

l.append(1)
l.append(2)
l.append(3)
l.append(4)

l.print()