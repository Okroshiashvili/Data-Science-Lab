"""
Created on Mon Jun 10 2019

@author: Nodar Okroshiashvili
"""




"""

Balanced Binary Trees(AVL) are much like binary search trees but in contrast to 
BST it has O(logN) time complexity.

Besides, AVL has balance factor which guarantees O(logN) time complexity.

One of the main property of AVL is the HEIGHT of a node, which is a length
of the longest path from this given node to a leaf node. Height for a
leaf node is -1. 

Height parameter couldn't differ more than one, or in other words

|height(left_subtree) - height(right_subtree)| <= 1

If left subtree and right subtree height parameter differ more than one, then
the tree is unbalanced and needs rotation.


AVL tree has balance factor, which is:
    balance factor = height(left_subtree) - heght(right_subtree)



"""



# First implement Node class

class Node:
    
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None



# Let implement AVL tree

class AVL:
    
    def __init__(self):
        self.root = None   # Initialize root node
        
    
    def insert(self, data):
        # On every insertion we have to check if we violate AVL property
        self.root = self.Insert_Node(data, self.root)
        
    def remove(self, data):
        if self.root:
            self.root = self.RemoveNode(data, self.root)
            
    
    def RemoveNode(self, data, node):
        
        if not node:
            return node
        
        if data < node.data:
            node.leftChild = self.RemoveNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.RemoveNode(data, node.rightChild)
        else:
            
            if not node.leftChild and not node.rightChild:
                print('Removing a leaf node...')
                del node
                return None
            
            if not node.leftChild:
                print('Removing a node with a right child...')
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('Removing a node with a left child...')
                tempNode = node.leftChild
                del node
                return tempNode
            
            print('Removing node with two children...')
            tempNode = self.get_Predecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.RemoveNode(tempNode.data, node.leftChild)
            
            
        if not node:
            return node # If the tree had just a single node
        
        node.height = max(self.calculate_height(node.leftChild),
                          self.calculate_height(node.rightChild)) + 1
        
        balance = self.calculate_balance(node)
        
        # Doubly left heavy situation
        if balance > 1 and self.calculate_balance(node.leftChild) >= 0:
            return self.right_rotation(node)
        
        # left-right situation
        if balance > 1 and self.calculate_balance(node.leftChild) < 0:
            node.leftChild = self.left_rotation(node.leftChild)
            return self.right_rotation(node)
        
        # Doubly right situation
        if balance < -1 and self.calculate_balance(node.rightChild) <= 0:
            return self.left_rotation(node)
        
        # right-left situation
        if balance < -1 and self.calculate_balance(node.rightChild) > 0:
            node.rightChild = self.right_rotation(node.rightChild)
            return self.left_rotation(node)
        
        return node
    
        
    
    
    def Insert_Node(self, data, node):
        
        if not node: # Check if node is empty
            return Node(data)
        
        if data < node.data:
            # Call Insert_Node method recursively
            node.leftChild = self.Insert_Node(data, node.leftChild)
        else:
            node.rightChild = self.Insert_Node(data, node.rightChild)
            
        # Calculate height
        node.height = max(self.calculate_height(node.leftChild),
                          self.calculate_height(node.rightChild)) + 1
        
        # Return node, but check if AVL property is violated
        # Let call violation method
        return self.settle_violation(data, node)
    
    
    
    
    def settle_violation(self, data, node):
        
        # First calculate balance
        balance = self.calculate_balance(node)
        
        # Case 1
        # left-left heavy situation, needs single right rotation
        # This situation means, that left subtree has more nodes than right subtree
        if balance > 1 and data < node.leftChild.data:
            print('Doubly left situation...')
            return self.right_rotation(node)
        
        
        # Case 2
        # right-right heavy situation, needs single left rotation
        # same as above, but in opposite direction
        if balance < -1 and data > node.rightChild.data:
            print('Doubly right situation...')
            return self.left_rotation(node)
        
        
        # Case 3
        # left-right heavy situation, needs left rotation
        # After left rotation we have left-left heavy situation
        # This need single right rotation
        if balance > 1 and data > node.leftChild.data:
            print('Left right situation...')
            node.leftChild = self.left_rotation(node.leftChild)
            return self.right_rotation(node)
        
        
        # Case 4
        # right-left heavy situation, needs right rotation
        # After this, we have right-right heavy situation
        # This need single left rotation
        if balance < -1 and data < node.rightChild.data:
            print('Right left situation...')
            node.rightChild = self.right_rotation(node.rightChild)
            return self.left_rotation(node)
        
        return node
        
    
    
    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)
	
    def traverseInorder(self, node):
        if node.leftChild:
            self.traverseInorder(node.leftChild)
        print("%s " % node.data)
        
        if node.rightChild:
            self.traverseInorder(node.rightChild)
    
    

        
    # Define some helper functions
    def calculate_height(self, node):
        if not node:   # This means node is None or has no any child
            return -1
        
        return node.height
    
    
    # Function for balance
    def calculate_balance(self, node):
        if not node:
            return 0   # Balance of leaf node is zero
        
        return self.calculate_height(node.leftChild) - self.calculate_height(node.rightChild)
    # If this function returns value more than 1, it means it is left heavy tree
    # and needs right rotation.
    # If ths function returns value less than -1, it means it is right heavy
    # tree and it needs left rotation.
    # If the function value is between -1 and 1, we don't need to rotate.
    




    # Below, we imlement left and rigth rotations. Rotation is very crucial
    # for AVL as it guarantees balance of trees
    def left_rotation(self, node):
        print("Rotating to the left on node", node.data)
        
        temp_RightChild = node.rightChild
        t = temp_RightChild.leftChild
        
        temp_RightChild.leftChild = node
        node.rigthChild = t
        
        # Calculate height
        node.height = max(self.calculate_height(node.leftChild),
                          self.calculate_height(node.rightChild)) + 1
                          
        
        temp_RightChild.height = max(self.calculate_height(temp_RightChild.leftChild),
                                     self.calculate_height(temp_RightChild.rightChild)) + 1
                            
        return temp_RightChild
    
    
    # Right rotation is almost the same as left rotation
    def right_rotation(self, node):
        print("Rotating to the right on node", node.data)
        
        temp_LeftChild = node.leftChild
        t = temp_LeftChild.rightChild
        
        temp_LeftChild.rightChild = node
        node.leftChild = t
        
        # Calculate height
        node.height = max(self.calculate_height(node.leftChild),
                          self.calculate_height(node.rightChild)) + 1
                          
        
        temp_LeftChild.height = max(self.calculate_height(temp_LeftChild.leftChild),
                                     self.calculate_height(temp_LeftChild.rightChild)) + 1
                            
        return temp_LeftChild
    
    def get_Predecessor(self, node):
        if node.rightChild:
            return self.get_Predecessor(node.rightChild)
        return node
    
        
    
        
    
  
# Testing the algorithm

avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)


avl.remove(15)
avl.remove(20)


avl.traverse()



## Resources
#
#https://runestone.academy/runestone/static/pythonds/Trees/AVLTreeImplementation.html
#
#https://algorithmtutor.com/Data-Structures/Tree/AVL-Trees/
#
#https://www.cs.usfca.edu/~galles/visualization/AVLtree.html


