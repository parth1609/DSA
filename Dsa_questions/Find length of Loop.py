'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        slow  = head
        fast  = head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
            if slow == fast:
                count = 1
                temp = slow
                while temp.next != slow:
                    count += 1
                    temp = temp.next
                return count
        return 0
    
