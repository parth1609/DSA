class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode(0)
        kurr = tmp
        summ = 0
        head = head.next 

        while head:
            if head.val == 0:
                kurr.next  =  ListNode(summ)
                kurr = kurr.next 
                summ =0
            else:
                summ += head.val
            head = head.next

        return tmp.next 
            

        
