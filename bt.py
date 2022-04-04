# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:18:41 2022

@author: hmdebern
"""


class Node:
    def __init__(self,data):
        self.data=data
        self.l_child=None
        self.r_child=None

class BTree:
    
    def __init__(self):
        self.root = None
      
    def insertNodeToNode(self,node,data):
        
        next_node=None
        
        if(node.data>data):
            next_node=node.l_child 
            if(next_node is None):
                new_node=Node(data)
                node.l_child=new_node
            else:
                self.insertNodeToNode(next_node,data)
                
        else:
            next_node= node.r_child
            if(next_node is None):
                new_node=Node(data)
                node.r_child=new_node
            else:
                self.insertNodeToNode(next_node,data)
        
         
    def insertNode(self,data):
        if(self.root is None):
            self.root= Node(data)
        else:
            self.insertNodeToNode(self.root,data)
            
    def inorderTraversal():
        self
    
        
        

tree =BTree()
tree.insertNode(8)
tree.insertNode(5)
tree.insertNode(9)
tree.insertNode(3)
tree.insertNode(4)
tree.insertNode(6)