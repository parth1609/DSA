

class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None
        
class Solution:
    def populateNext(self, root):
        result = []
        def help(node):
            if node:
                help(node.left)
                result.append(node)
                help(node.right)
        help(root)
        
        for i in range(len(result)-1):
            result[i].next = result[i+1]
