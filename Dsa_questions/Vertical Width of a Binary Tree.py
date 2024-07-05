class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

#Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    if not root:
        return 0 
     
    l = float("inf")  
    r = float("-inf")  
    
    def dfs(node,skew):
        nonlocal l,r
        if not node:
            return  

        if node.left:
            dfs(node.left, skew-1)
            
        l = min(l,skew)
        r = max(r,skew)
            
        if node.right:
            dfs(node.right, skew+1)
        
    dfs(root,0)
    
    return r-l+1
            
