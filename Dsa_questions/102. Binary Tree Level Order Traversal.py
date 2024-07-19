from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        li = deque([root])
        while li:
            n= len(li)
            inner = []
            
            for _ in range(n):
                node = li.popleft()
                inner.append(node.val)
                if node.left:
                    li.append(node.left)
                if node.right:
                    li.append(node.right)
            ans.append(inner)
        return ans
