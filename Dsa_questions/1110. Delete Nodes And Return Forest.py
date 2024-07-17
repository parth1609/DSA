# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deletehelper(self,root,to_delete,result):
        if root is None:
            return None 
        
        root.left  =  self.deletehelper(root.left,to_delete,result)
        root.right =  self.deletehelper(root.right,to_delete,result)

        if root.val in to_delete:
            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
            return None

        return root

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete_set = set(to_delete)  # Use a set for O(1) lookup time

        if root and root.val not in to_delete_set:
            result.append(root)

        self.deletehelper(root, to_delete_set, result)
        return result
