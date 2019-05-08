
"""
Created on Mon May  6 2019

@author: Nodar Okroshiashvili
"""


# This class defines new nodes of linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# This class defines itself linked list
# Here goes all methods of linked list, such as insertion, deletion and so on
class LinkedList:
    def __init__(self):
        self.start = None

    # Implement "insert" function to do data insertion
    def insert(self, value): # value parameter is data we want to insert
        # First we need to check is linked list is empty or not
        if self.start == None:# means our linked list is empty
            self.start = Node(value)
            return
        # If linked list is ot empty we want to add element at the end
        # For this we need variable which move though every node of
        # our linked list and get to the ending position
        current = self.start

        while current.next is not None:
            current = current.next
            # When this loop end, this means we are at the end of lined list
            # and we can isert new elemet
        current.next = Node(value) # insert new element at the end

    def print(self):
        current = self.start

        while current is not None:
            print(current.value)
            current = current.next

    def delete_first_node(self):
        # Check if linked list is empty
        if self.start == None:
            return

        self.start = self.start.next

    def delete_last_node(self):
        # Check if linked list is empty
        if self.start == None:
            return

        current = self.start

        while current.next.next is not None:
            current = current.next
        current.next = None














"""

Test our linked list class

"""

linkedlist = LinkedList()

linkedlist.insert(10)
linkedlist.insert(20)
linkedlist.insert(40)
linkedlist.insert(30)
linkedlist.insert(50)

linkedlist.print()


linkedlist.delete_first_node()
linkedlist.print()


linkedlist.delete_last_node()
linkedlist.print()





"""

Traversing a Linked List means printing all the values of a Linked List


###

If we have linked list, we need to have a loop that will move though every
value of this linked list and print them.




###

Now we know how to insert new element is linked list.

But, how can we delete node?
There are three possibilities to delete node in linked list.

First is to delete starting node.
Second is to delete node in somewhere middle of linked list
Third is to delete the end node of linked list

"""
