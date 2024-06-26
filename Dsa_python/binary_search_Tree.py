import random

# The provided Python class implements a binary search tree (BST) with methods for insertion, search,
# traversal, finding minimum and maximum values, deletion, calculating size, and determining the
# height of the tree.


# This class defines a node with an item, left child, and right child attributes.
class node:
    def __init__(self,itm= None,left = None,right = None):
        self.itm = itm
        self.left = left
        self.right = right

class BST:
    def __init__(self,root = None):
        """
        The function is a Python constructor that initializes an object with a root attribute, which
        defaults to None if not provided.
        
        :param root: The `__init__` method is a special method in Python classes used for initializing
        new objects. In this case, the `__init__` method takes one parameter `root`, with a default
        value of `None`. This parameter is used to initialize the `root` attribute of the object being
        """
        self.root = root
        

     # use recursive function rinsert() to insert itm
    def insert(self, data):
        """
        The function `insert` recursively inserts a node with the given data into a binary search tree.
        
        :param data: The `data` parameter in the `insert` method represents the value that you want to
        insert into the binary search tree. It is the data that you want to store in the tree node
        """
        self.root = self.rinsert(self.root,data)
        
    
    def rinsert(self,root,data):
        if root is None:
            return node(data)
        if data < root.itm:
            root.left = self.rinsert(root.left,data)
        elif data > root.itm:
            root.right = self.rinsert(root.right,data)
        return root

 # use recursive function rsearch() 
    def search(self,data):
        """
        The function performs a recursive search for a specific data item in a binary search tree.
        
        :param data: The `data` parameter in the code represents the value that is being searched for in
        a binary search tree. The `search` method is used to initiate the search process by calling the
        `rsearch` method with the root of the tree and the target `data` value. The `rsearch
        :return: The `search` method is being called with the `data` parameter, which then calls the
        `rsearch` method with the root node and the `data` parameter. The `rsearch` method recursively
        searches for the `data` in the binary search tree starting from the root node. If the `data` is
        found in the tree, the method returns the node containing the `data`.
        """
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if root is None or root.itm == data:
            return root
        if data < root.itm:
            return self.rsearch(root.left,data)
        elif data >root.itm:
            return self.rsearch(root.right, data)
    

# Depth first traversal
    # return in inorder (left,root,right) 
    #  use recursive function rinorder() 
    def inorder(self):
        """
        The function performs an inorder traversal on a binary tree and returns the elements in a list.
        :return: The `inorder` method is returning a list of items in the binary tree in inorder
        traversal.
        """
        result = []
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result) 
            result.append(root.itm)
            self.rinorder(root.right,result)

    # return in preorder (root,left,right) 
    #  use recursive function rpreorder() 
    def preorder(self):
        """
        The function performs a preorder traversal on a binary tree and returns a list of the nodes
        visited in the traversal.
        :return: The `preorder` method is returning a list of items in the binary tree in preorder
        traversal order.
        """
        result = []
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:
            result.append(root.itm)
            self.rpreorder(root.left,result) 
            self.rpreorder(root.right,result)

    # return in postorder (left,right,root) 
    #  use recursive function rpostorder() 
    def postorder(self):
        """
        The function performs a postorder traversal on a binary tree and returns a list of items in the
        traversal order.
        :return: The `postorder` method is being called on a binary tree object. This method performs a
        postorder traversal of the binary tree starting from the root node. The traversal visits the
        left subtree, then the right subtree, and finally the root node. The method returns a list of
        items in postorder traversal order.
        """
        result = []
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result) 
            self.rpostorder(root.right,result)
            result.append(root.itm)

    # minimum Value in BST on the left most side
    def min_val(self,tmp):
        """
        The `max_val` function finds and returns the maximum value in a linked list starting from a
        given node.
        
        :param tmp: The `tmp` parameter in the provided code snippets represents a node in a binary
        search tree (BST) data structure. The `min_val` function finds and returns the minimum value in
        the BST by traversing to the leftmost node starting from the given node `tmp`. Similarly, the
        `max
        :return: The `max_val` function is returning the maximum value found in the linked list starting
        from the given node `tmp`.
        """
        current = tmp
        while current.left is not None:
            current = current.left
        return current.itm
    
    # minimum Value in BST on the right most side
    def max_val(self,tmp):
        """
        This function finds and returns the maximum value in a linked list starting from a given node.
        
        :param tmp: It looks like the code you provided is a method called `max_val` that takes a
        parameter `tmp`. The method is designed to find and return the maximum value in a data structure
        represented by the variable `tmp`
        :return: The code snippet provided is a method called `max_val` that takes a parameter `tmp`. It
        iterates through the linked list starting from the node `tmp` and traverses to the rightmost
        node in the list. Finally, it returns the value stored in the rightmost node, which is denoted
        by `current.itm`.
        """
        current = tmp
        while current.right is not None:
            current = current.right
        return current.itm
    
     # use recursive function rdelete() to delete itm
    def delete(self,data):
        """
        The given Python code defines a recursive function `rdelete()` to delete a specified item from a
        binary search tree.
        
        :param data: The `data` parameter in the `delete` function represents the item that you want to
        delete from the binary search tree. The `rdelete` function is a recursive function that
        traverses the tree to find and delete the specified item (`data`). If the item is found, it is
        removed from
        """
        self.root = self.rdelete(self.root,data)
        

    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.itm:
            root.left = self.rdelete(root.left,data)
        elif data > root.itm:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.itm = self.min_val(root.right)
            self.rdelete(root.right,root.itm)
        return root
    
    def size(self):
        # The line `return len(self.inorder())` in the provided code snippet is part of the `size()`
        # method within the Binary Search Tree (BST) class. This method is used to calculate and
        # return the number of nodes in the binary search tree.
        return len(self.inorder())
    

# Breadth first Transversal


    def height(self, root):
        """
        The function calculates the height of a binary tree rooted at the given node.
        """
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1



    
    def merge_trees(self, tree1, tree2):
        # The provided code snippet defines a method named `merge_trees` within the Binary Search
        # Tree (BST) class. This method is used to merge two binary search trees into a single binary
        # search tree.
        if tree1 is None:
            return tree2
        if tree2 is None:
            return tree1
        
        merged_node = node(tree1.itm + tree2.itm)
        # Recursively merge the left subtrees
        merged_node.left = self.merge_trees(tree1.left, tree2.left)
        # Recursively merge the right subtrees
        merged_node.right = self.merge_trees(tree1.right, tree2.right)
        return merged_node



        # T1 = BST()
        # T1.insert(30)
        # T1.insert(40)

        # T2 = BST()
        # T2.insert(5)

        # tree3 = BST()
        # tree3.root = tree3.merge_trees(T1.root, T2.root)
        # print(tree3.inorder())


    def sum_all_node(self,root):
        """
        This Python function recursively calculates the sum of all nodes in a binary tree starting
        from the root node.
        """
        return self.rsum_node(self.root)
    
    def rsum_node(self,root):
        if root is None:
            return 0
        else:
            left_sum = self.rsum_node(root.left)
            right_sum = self.rsum_node(root.right)
            return  root.itm + left_sum + right_sum
    

    # Nsum = BST()
    # Nsum.insert(1)
    # Nsum.insert(2)
    # Nsum.insert(3)
    # print(Nsum.sum_all_node(Nsum.root))
        


    def sum_left_leaf(self,root):
        if root is None:
            return 0
        lftsum = 0
        if root.left:
            if root.left.left is None and root.right.left is None:
                lftsum += root.left.itm
            else:
                lftsum += self.sum_left_leaf(root.left)
        lftsum += self.sum_left_leaf(root.right)
        return lftsum
        


    # Nsum = BST()
    # Nsum.insert(20)
    # Nsum.insert(10)
    # Nsum.insert(35)
    # Nsum.insert(9)
    # Nsum.insert(25)
    # Nsum.insert(12)
    # Nsum.insert(52)
    # print(Nsum.sum_left_leaf(Nsum.root))