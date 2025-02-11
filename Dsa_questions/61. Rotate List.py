# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def FindlastNode(self,head,k):
        tmp = head
        k-=1
        while k>0:
            k-=1
            tmp = tmp.next
        return tmp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        tmp = head
        length = 1
        while tmp.next:
            tmp = tmp.next
            length+=1
        tmp.next = head
        k = k % length
        end  = length-k
        while end:
            tmp = tmp.next
            end -= 1
        head = tmp.next
        tmp.next = None

        return head

        

        
