# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        removal = set(nums)
        while head and head.val in removal:
            head = head.next 
        if not head:
            return 
        current = head
        while current.next:
            if current.next.val in removal:
                current.next  = current.next.next 
            else:
                current = current.next 

        return head



        
