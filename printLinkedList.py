# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:12:27 2022

@author: hmdebern
"""

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    print(head.data)
    if(head.next != None):
        printLinkedList(head.next)

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
