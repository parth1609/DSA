# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or head.next.next is None:
            return [-1,-1]

        FirstCriticalIndex =0
        PreviousCriticalIndex = 0
        minimumDistance = float('inf')
        maximumDistance = float('inf')

        prv = head
        tmp = head.next 
        i = 1
        
        while tmp and tmp.next:
            nxt = tmp.next 

            if (tmp.val < prv.val and tmp.val < nxt.val) or (tmp.val > prv.val and tmp.val > nxt.val):
                if FirstCriticalIndex == 0:
                    FirstCriticalIndex = i
                else:
                    minimumDistance = min(minimumDistance, i - PreviousCriticalIndex)
                    maximumDistance = i - FirstCriticalIndex
                PreviousCriticalIndex = i
            
            prv = tmp
            tmp = nxt
            i+=1
        if minimumDistance == float('inf'):
            return [-1,-1]
        
        return [minimumDistance,maximumDistance]
                
        
