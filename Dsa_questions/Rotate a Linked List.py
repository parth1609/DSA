'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if head is None:
            return None 
        
        current  =  head
        count  = 1
        while count < k and current.next is not None:
            current = current.next 
            count += 1
        
        kth_current  = current 
       
        while current.next is not None:
            current = current.next 
        
        current.next =  head
        head = kth_current.next 
        kth_current.next  = None 
        
        return head
        
