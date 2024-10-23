
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next 
        while fast is not None:
            fast = fast.next 
            slow = slow.next 
        summ =0
        while slow is not None:
            summ += slow.data
            slow  = slow.next 
        
        return summ
        
    
