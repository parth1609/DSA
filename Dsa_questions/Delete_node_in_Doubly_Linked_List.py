# Delete node in Doubly Linked List

class Solution:
    def delete_node(self, head, x):
        #code here
        if x==1:
            head = head.next 
        
        tmp = head
        count = 1
        
        while tmp.next is not None and count < x:
            tmp = tmp.next 
            count +=1
        
        if tmp is not None:
            if tmp.next:
                tmp.next.prev = tmp.prev 
            if tmp.prev:
                tmp.prev.next = tmp.next 
        
        return head       
            
