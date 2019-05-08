"""
Created on Tue May  7 2019

@author: Nodar Okroshiashvili
"""







"""

Tree is a type of nonlinear data strycture, where data is connected to each
other in hierarchy. Every conteiner of data is called node. Top node is
called root node, and nodes at the end of tree are called leaf nodes.



"Binary Search Tree is a type of data structure which have at most
two children. It cannot have more than two children.

Every node of the tree has to have at moset 2 child. This is BST


In BST, smaller nodes are at the left of root node and bigger nodes
are at the right side of root node. This procedure is reapeted for every
sub tree, untill we find appropriate place for new node.

"""





# Create  Node class for Binary Search Tree

class Node:
    
    # Constructor
    def __init__(self,value): # value parameter is data we want to store
        self.value = value
        self.left = None # At the start we have no left node
        self.right = None # At the start we have no right node
    

# Insert method to insert new node in BST
def insert(root,node): # Insert is recursive function
    if root is None: # Base condition
        root = node
        return root
    
    if node.value < root.value:
        root.left = insert(root.left, node)
    
    if node.value > root.value:
        root.right = insert(root.right, node)
    
    return root
    
        

# Let implement various types of traversal of BST. This means to print
# nodes on the screen.
    

# First, implement pre-order traversal. In pre-order traversal, we print
# the value of root in the first place, after that we'll print left child
# and then right child and this sequace of root, left, and right should be
# followed for every subtree of BST.
    
def pre_order(root):
    if root: # Check if root is empty, and then print left and then right node
        print(root.value)
        pre_order(root.left)
        pre_order(root.right)




# Now implement In-order traversal. This means to print root value in the center
# In this type of traversal, left child is printed first, then root is printed
# and then right node is printed. This sequance has to be folloewd for every
# subtree.

def in_order(root):
    if root:
        in_order(root.left)
        print(root.value)
        in_order(root.right)




# Implement Post-order traversal of BST. This means to print the root in the end.
# In this type of traversal, left node is printed first, then right node and
# in the last root node is printed.
# This sequance has to be followed for every subtree.

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value)




# Finding a minimum value node in BST is very important when it comes to delete
# a node in BST. Below we implement method to find minimum value node.
# From above comments, we know that minimum value node is always the left
# most in BST.

def get_minimum_value_node(root):
    if root:
        while root.left is not None:
            root = root.left
        return root


# Find maximum value node

def get_maximum_value_node(root):
    if root:
        while root.right is not None:
            root = root.right
        return root



# When we want to delete node in BST, there are three possibilities.
# First possibility is to delete node which is leaf node and has no any child.
# Second possibility is to delete node which has one child.
# When we do this kind of deletion, child node of deleted root node will
# take it's parent's place.
# Third possibility is to delete node which has both child, left node and
# right node. In this case we have to find the node which will take deleted
# node's position, so that BST maintain it's order.

def delete_node(root,value):
    if root is None: # Base condition
        return root
    # We need to find value in our BST
    if value < root.value:
        root.left = delete_node(root.left, value)
    
    elif value > root.value:
        root.right = delete_node(root.right, value)
        # else part will only go when the value will be found
    else:
        if root.left is None: # First possibility
            temp = root.right
            root = None
            return temp
        elif root.right is None: # Second possibility
            temp = root.left
            root = None
            return temp
        else: # Third possibility
            temp = get_minimum_value_node(root.right)
            root.value = temp.value
            
            root.right = delete_node(root.right, temp.value)
    return root
            





"""
Test our class of BST

"""

# Initialize Node class and set initial value
root = Node(50)

# Insert new node
insert(root, Node(10))
insert(root, Node(2))
insert(root, Node(80))
insert(root, Node(15))
insert(root, Node(60))
insert(root, Node(90))

# Pre-order traversal
pre_order(root)

# In-order traversal
in_order(root)

# Post-order traversal
post_order(root)

# Get minimum value node
get_minimum_value_node(root).value # .value gives actual value of a node

# Get maximum value node
get_maximum_value_node(root).value

# Delete main root node
delete_node(root,50)

# Post-order traversal to see the new BST values
post_order(root)

# http://interactivepython.org/lpomz/courselib/static/pythonds/Trees/SearchTreeImplementation.html
