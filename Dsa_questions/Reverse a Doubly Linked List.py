'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        prev = None
        tmp = head
        while tmp:
            tmp.prev = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = tmp.prev
        return prev
            
