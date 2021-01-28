# Reverse linked list is quite a notorious problem, isn't it?
# It's actually quite simple if you use three pointers 

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = next 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head 
        prev = None 
        while curr:
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node 
        return prev
