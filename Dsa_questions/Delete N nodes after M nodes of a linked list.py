'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        
        tmp = head
        prv = None 
        while tmp:
            for _ in range(m):
                if not tmp:
                    return head 
                prv = tmp
                tmp = tmp.next 
            
            
            for _ in range(n):
                if not tmp:
                    return head 
                tmp = tmp.next
                prv.next = tmp
