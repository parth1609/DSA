'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def newNode(self, data):
        return Node(data)
    
    def reverselist(self,head):
        if not head:
            return 
        prv_node = head
        cur_node = head
        Next_node = head.next 
        cur_node.next = None 
        
        while Next_node:
            cur_node = Next_node
            Next_node = Next_node.next 
            cur_node.next = prv_node
            prv_node = cur_node
        
        return cur_node
        
    def addOne(self,head):
        head = self.reverselist(head)
        k = head
        carry = 0
        prv = None 
        head.data += 1
        
        while head and (head.data > 9 or carry > 0):
            prv = head
            head.data += carry 
            carry = head.data // 10
            head.data = head.data % 10
            head = head.next 
            
        if carry > 0:
            prv.next = self.newNode(carry)
            
        
        return self.reverselist(k)     
        
        
