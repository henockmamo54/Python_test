# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:35:03 2022

@author: hmdebern
"""


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
        
    
def topView(root):
    #Write your code here  
        if(root == None):
            return
        
        root.hd=0
        vals=[]
        vals_hd=[]
        q=[root]
        
        while(len(q)):
            
            node= q.pop(0)
            
            if(node.hd not in vals_hd):
                vals.append((node.info))
                vals_hd.append(node.hd)
            
            if(node.left):
                node.left.hd=node.hd-1
                q.append(node.left)
                
            if(node.right):
                node.right.hd=node.hd+1
                q.append(node.right)
             
        # vals=list(set(vals))
        # vals.sort() 
        sortedvals=map(str, vals)
        print(" ".join(sortedvals))
            
            
        


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)