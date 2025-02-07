'''
# Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
                self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        tmp = head
        while tmp:
            nextNode = tmp.next
            while nextNode and nextNode.data == tmp.data:
                nextNode = nextNode.next
            if nextNode:
                nextNode.prev = tmp
            tmp.next = nextNode if nextNode else None
            tmp = tmp.next
            
        return head
