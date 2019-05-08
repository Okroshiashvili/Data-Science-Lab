"""
Created on Mon May  6 2019

@author: Nodar Okroshiashvili
"""




"""

Here I implement "Single Linked List"


"""



# Let first define node class
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


# This class defines itself linked list
# Here goes all methods of linked list, such as insertion, deletion and so on
class LinkedList:
    def __init__(self):
        self.start = None

    # Implement "insert" function to do data insertion.

    # But before implementing insertion method it's good idea
    # to implement linked list traversing.
    # Traversing a Linked List means printing all the values
    # of a Linked List.
    # If we have linked list, we need to have a loop that will move
    # though every value of this linked list and print them.
    def traverse_list(self):
        # The first part of this function is to check if list is empty
        if self.start == None:
            print('List is empty')
            return
        # If list is not empty then below code will execute
        # and print all elements of a linked list
        else:
            current = self.start

            while current is not None:
                print(current.value)
                current = current.next
        # The above else block states that if the reference of node
        # is not None (meaning it's not last element) then print it
        # and set current node's reference equal to the next nodes
        # reference. If next node's reference is None then while
        # loop terminates.


        """
        Insertion methods

        """

        # Depending on your will, where to insert node in the linked list
        # there are different methods

        # Let first define insert method to insert element at the start

    def insert_at_start(self,data):# data parameter is data we want to insert
        new_node = Node(data)
        new_node.next = self.start
        # Since the new_node is the first node, set value of the
        # start variable to new_node
        self.start = new_node
            
        
    # Insert node at the end of linked list
    def insert_at_end(self,data):
        # This function has two block
        
        # First block checks if linked list is emptry
        # If it is, then set variable start to new_node
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
            return
        # Second block
        # If list already contains nodes we have to initialize
        # variable current with the start node
        current = self.start
        
        # Let iterate though all nodes. The while loop terminates when we
        # reach the last node and then adds new node after previous
        # last node.
        # When this loop end, this means we are at the end of linked list
        # and we can isert new elemet
        while current.next is not None:
            current = current.next
        current.next = new_node # insert new element at the end
            
            
            
    # Insert new value after another value
    def insert_after_value(self, x, data):
        # First parameter "x" is the value after which we want to
        # insert the new value. And parameter "data" is the
        # new value or new node we want to insert
        
        # In other words, "x" is the existing node and after that
        # node we want to insert "data".
        current = self.start
        print(current.next)
        
        while current is not None:
            if current.value == x:
                break
            current = current.next
        # This while loop executes until "current" becomes None.
        # During each iteration check if the value stored in
        # current node is equal to the "x" parameter.
        # If this is the case then break the loop
        
        # second part
        
        # If the value is found, "current" variable will not be None
        # The reference of the new_node is set to the reference
        # stored by "current" and the reference of "current"
        # is set to "new_node"
        if current is None:
            print('Value not in the list')
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            
            
    # Insert new value before anther value
    def insert_before_value(self, x, data):
        # This function have three parts
        
        # First part check if list is empty and if it is, returns
        if self.start == None:
            return
        
        # Second, check if the node is located at the first index
        if x == self.start.value:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node
            return
        # If the node after which we want to insert new node is
        # located at the first index, then set the reference of new
        # node the reference of start node and then set value of
        # start node to the value of newly added node
        # In other words this code interchanges the place of start node
        # and newly added node, so that newly added node is before
        # start node.
        
        # Third part
        current = self.start
        print(current.next)
        
        while current.next is not None:
            if current.next.value == x:
                break
            current = current.next
            
        if current.next is None:
            print('Value not in the list')
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
                    
                    
    # Inser node at specific index
    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node
        # Above if flow is the same as to insert at the start of list
        
        i = 1
        current = self.start
        
        while i < index -1 and current is not None:
            current = current.next
            i = i + 1
        if current is None:
            print('Index out of bound')
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
                    


"""
So far, so good. Let test our linked list class and method we implemented

"""


# Initialize empty linked list

linkedlist = LinkedList()


# Inser new node at the start
linkedlist.insert_at_start(10)

# Traverse the linked list
linkedlist.traverse_list()


# Insert new node at the end
linkedlist.insert_at_end(50)

linkedlist.traverse_list()

# Insert new note at specific index
linkedlist.insert_at_index(2,30)

linkedlist.traverse_list()


# Insert new node before some value
linkedlist.insert_before_value(30,20)

linkedlist.traverse_list()


# Insert new node after some value
linkedlist.insert_after_value(30,40)

linkedlist.traverse_list()


# Reference
# https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/#singlelinkedlist







