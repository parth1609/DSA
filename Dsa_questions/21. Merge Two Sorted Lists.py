# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tmp = dummy
        tmp1 = list1
        tmp2 = list2
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                tmp.next = tmp1
                tmp1 = tmp1.next
                tmp = tmp.next
            else:
                tmp.next = tmp2
                tmp2 = tmp2.next
                tmp = tmp.next
        if tmp1:
            tmp.next = tmp1
        else:
            tmp.next = tmp2
        return dummy.next

        
