# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Let's implement a small test for the corrected solution.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None 
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

    def findpath(self, root, target, path):
        if root is None:
            return False
        if root.val == target:
            return True
        
        path.append("L")
        if self.findpath(root.left, target, path):
            return True
        path.pop()
        
        path.append("R")
        if self.findpath(root.right, target, path):
            return True
        path.pop()
        
        return False

    def find_node(self, root, val):
        if root is None:
            return None 
        if root.val == val:
            return root
        left = self.find_node(root.left, val)
        if left:
            return left 
        return self.find_node(root.right, val)

    def getDirections(self, root: 'TreeNode', startValue: int, destValue: int) -> str:
        startNode = self.find_node(root, startValue)
        destNode = self.find_node(root, destValue)
        
        LCA = self.lowestCommonAncestor(root, startNode, destNode)
        
        path_to_start = []
        path_to_dest = []
        
        self.findpath(LCA, startValue, path_to_start)
        self.findpath(LCA, destValue, path_to_dest)
        
        path_to_start = ['U'] * len(path_to_start)
        
        result = ''.join(path_to_start) + ''.join(path_to_dest)
        return result
