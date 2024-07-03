# Remove all occurences of duplicates in a linked list

#User function Template for python3

"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""

class Solution:
    def removeAllDuplicates(self, head):
        
        zero_Node = Node(0)
        zero_Node.next = head
       
        tmp = zero_Node
        while tmp.next and tmp.next.next:
            if tmp.next.data == tmp.next.next.data:
                repeat_val = tmp.next.data
                while tmp.next and tmp.next.data == repeat_val:
                    tmp.next = tmp.next.next 
            else:
                tmp = tmp.next 
        
        return zero_Node.next   
        
