class Solution:
    def isroot(self,root):
        if root is None:
            return None
        if (root.left is not None and root.right is None) or (root.left is  None and root.right is not None):
            return True
        return False 
       
    def RemoveHalfNodes(self, root):
        #code here
        if root is None:
            return None 
        root.left =  self.RemoveHalfNodes(root.left)      
        root.right =  self.RemoveHalfNodes(root.right)      
        if self.isroot(root):
            if root.left is not None:
                return root.left 
            else:
                return root.right
            
        return root
