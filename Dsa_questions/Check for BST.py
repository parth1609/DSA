
class Solution:
    def istrue(self,root,left,right):
        if root is None:
            return True 
        if root.data <= left or root.data >= right:
            return False 
        
        return (self.istrue(root.left, left, root.data) and self.istrue(root.right, root.data, right))
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.istrue(root,float('-inf'), float('inf'))
