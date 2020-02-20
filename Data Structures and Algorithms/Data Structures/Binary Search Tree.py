


"""
Tree is a type of nonlinear data stricture, where data is connected to each
other in hierarchy. Every container of data is called node. Top node is
called root node, and nodes at the end of tree are called leaf nodes.

"Binary Search Tree is a type of data structure which have at most
two children. It cannot have more than two children.

Every node of the tree has to have at most 2 child. This is BST


In BST, smaller nodes are at the left of root node and bigger nodes
are at the right side of root node. This procedure is repeated for every
sub tree, until we find appropriate place for new node.

"""



class Node:
    
    # Constructor
    def __init__(self,value): # value parameter is data we want to store
        self.value = value
        self.left = None # At the start we have no left node
        self.right = None # At the start we have no right node


def insert(root,node): # Insert is recursive function
    if root is None: # Base condition
        root = node
        return root
    
    if node.value < root.value:
        root.left = insert(root.left, node)
    
    if node.value > root.value:
        root.right = insert(root.right, node)
    
    return root

    
def pre_order_traversal(root):
    """
    Pre-Order traversal. In pre-order traversal, print the root first,
    after that print left child and than right child. 
    This pattern has to be true for all subtree.
    """
    if root: # Check if root is empty, and then print left and then right node
        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def in_order_traversal(root):
    """
    In-Order traversal prints left child first, 
    then root and then right child. This pattern has to be true 
    for all subtree.
    """
    if root:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)


def post_order_traversal(root):
    """
    Post-Order traversal prints left node first, then right node
    and then root node. This pattern repeats for every subtree.
    """
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)


def get_minimum_value_node(root):
    """
    Get the node with the minimum value.
    
    The minimum value node is always left most in the BST
    """
    if root:
        while root.left is not None:
            root = root.left
        return root


def get_maximum_value_node(root):
    """
    Get the node with the maximum value

    The maximum value node is always right most in the BST
        """
    if root:
        while root.right is not None:
            root = root.right
        return root


"""
When we want to delete node in BST, there are three possibilities.

First possibility is to delete node which is leaf node and has no any child.

Second possibility is to delete node which has one child.
When we do this kind of deletion, child node of deleted root node will
take it's parent's place.

Third possibility is to delete node which has both child, left node and
right node. In this case we have to find the node which will take deleted
node's position, so that BST maintain it's order.

"""


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
pre_order_traversal(root)

# In-order traversal
in_order_traversal(root)

# Post-order traversal
post_order_traversal(root)

# Get minimum value node
get_minimum_value_node(root).value # .value gives actual value of a node

# Get maximum value node
get_maximum_value_node(root).value

# Delete main root node
delete_node(root,50)

# Post-order traversal to see the new BST values
post_order_traversal(root)




# # Resource
# http://interactivepython.org/lpomz/courselib/static/pythonds/Trees/SearchTreeImplementation.html



