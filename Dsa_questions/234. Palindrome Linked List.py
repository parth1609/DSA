# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        prev = None
        tmp = head
        while tmp:
            front = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        newhead = self.reverse(slow.next)
        first = head
        second = newhead
        while second:
            if first.val != second.val:
                self.reverse(newhead)
                return False
            first = first.next
            second = second.next
        self.reverse(newhead)
        return True
      

