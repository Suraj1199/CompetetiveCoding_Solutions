"""
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        s = []
        while head:
            s.append(head.data)
            head = head.next
        l = Node(0)
        i = l
        while s:
            i.next = Node(s[-1])
            i = i.next
            s.pop()
        return l.next
