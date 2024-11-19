# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp  = ListNode()
        kurr = tmp
        carry = 0
        while l1 or l2 or carry != 0:
            sum_ = carry 
            if l1:
                sum_ += l1.val
                l1 = l1.next 
            if l2:
                sum_ += l2.val
                l2 = l2.next 
            carry = sum_ // 10
            kurr.next = ListNode(sum_ % 10)
            kurr = kurr.next 

        return tmp.next 



        
