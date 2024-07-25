class node:
    def __init__(self,data= None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root=None):
        self.root = root
        
        
    def sortedArrayToBST(self, nums):
        # code here
        if not nums:
            return None
            
        n = len(nums)
        i = 0
        j = n-1
        mi = (i + j)//2
        root = node(nums[mi])
        root.left = self.sortedArrayToBST(nums[:mi])
        root.right = self.sortedArrayToBST(nums[mi+1:])
        
        return root
