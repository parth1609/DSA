'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        # code here
        def ispath(root, target,pathsum):
            if root is None:
                return False
        
            pathsum += root.data
        
            if root.left is None and root.right is None :
                return pathsum == target
            
            return ispath(root.left, target, pathsum) or ispath(root.right, target, pathsum)
        return ispath(root, target, 0)
          
