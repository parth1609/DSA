# 1382. Balance a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        arr = []
        def inorder(root,arr):
            if root:
                inorder(root.left,arr)
                arr.append(root.val)
                inorder(root.right,arr) 
        def bst(arr, l,r):
            if l>r:
                return None 
            mi = (l + r) // 2
            left = bst(arr,l,mi-1) 
            right = bst(arr,mi+1,r) 
            return TreeNode(arr[mi],left,right)
        
        inorder(root,arr)
        return bst(arr,0, len(arr)-1) 
