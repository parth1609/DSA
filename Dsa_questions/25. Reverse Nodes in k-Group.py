# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Reverselist(self,head):
        prev = None 
        tmp = head
        while tmp:
            Next = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = Next
        return prev
    
    def kthNode(self,tmp,k):
        k-=1
        while tmp and k>0:
            k-=1
            tmp = tmp.next

        return tmp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        PrevLast = None
        while tmp:
            kthnode = self.kthNode(tmp,k)
            if kthnode is None:
                if PrevLast:
                    PrevLast.next = tmp
                break

            NextNode = kthnode.next
            kthnode.next = None
            self.Reverselist(tmp)
            if tmp == head:
                head = kthnode
            else:
                PrevLast.next = kthnode
            PrevLast = tmp
            tmp = NextNode
        return head


        
