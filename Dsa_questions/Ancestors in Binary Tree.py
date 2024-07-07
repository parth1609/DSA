'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def findAncestors(self, root,target, ancestors):
        if root is None:
            return None 
        
        if root.data == target:
            return True
            
        left  = self.findAncestors(root.left, target,ancestors)
        right  = self.findAncestors(root.right, target,ancestors)
        if left or right:
            ancestors.append(root.data)
            return True
        return False 

    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        ancestors = []
        self.findAncestors(root,target,ancestors)
        return ancestors
        
