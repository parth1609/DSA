# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent, child,isleft in  descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            if isleft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child)
        
        root = None
        for node in nodes:
            if node not in children:
                root = nodes[node]
                break 
        return root
