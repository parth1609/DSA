

'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent):
        # your code here
        nodes = {}
        for i in range(len(parent)):
            nodes[i] = Node(i)
        
        root = None 
        
        for i in range(len(parent)):
            if parent[i] == -1:
                root = nodes[i]
            else:
                if not nodes[parent[i]].left:
                    nodes[parent[i]].left = nodes[i]
                else:
                    nodes[parent[i]].right = nodes[i]
            
        return root
