'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        # code here
        if head is None:
            return None 
           
        tmp = head
        while tmp and tmp.next:
            tmp.next = tmp.next.next 
            tmp = tmp.next 
        return head
