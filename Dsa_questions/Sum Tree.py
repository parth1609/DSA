 
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def is_sum_tree(self, root):
        # code here
        if root is None:
            return None 
        if root.left == None and root.right == None:
            return root
        rootsum = 0
        if root.left:
            rootsum += root.left.data
            if root.left.left and root.left.right:
                rootsum += root.left.data
                
        if root.right:
            rootsum += root.right.data
            if root.right.left and root.right.right:
                rootsum += root.right.data
        
        if rootsum == root.data and self.is_sum_tree(root.left) and self.is_sum_tree(root.right):
            return True
        return False 
