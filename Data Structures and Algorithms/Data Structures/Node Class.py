


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        """
        Initialize empty Linked List
        """
        self.start = None


    # Implement "insert" function to do data insertion
    def insert(self, value: int):
        """
        Takes value and inserts it in the  Linked List

        Args:
            value: Value to instert
        """
        # Check if Linked List is empty or not
        if self.start == None:
            self.start = Node(value)
            return
        # If linked list is not empty we want to add element at the end
        # For this we need variable which move though every node of
        # our linked list and get to the ending position
        current = self.start

        while current.next is not None:
            current = current.next
            # When this loop end, this means we are at the end of linked list
            # and we can insert new element
        current.next = Node(value) # insert new element at the end


    def print(self):
        """
        Print the values of the Linked List
        """
        current = self.start

        while current is not None:
            print(current.value)
            current = current.next


    def delete_first_node(self):
        """
        Removes the first node from the Linked List
        """
        if self.start == None:
            return

        self.start = self.start.next


    def delete_last_node(self):
        """
        Removes the last node from the Linked List
        """
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


