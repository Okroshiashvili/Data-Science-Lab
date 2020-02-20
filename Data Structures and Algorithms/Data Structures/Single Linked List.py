


class Node:
    
    def __init__(self, data):
        self.value = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.start = None


    def traverse_list(self):
        """
        Loops through every value of this single linked list and print them
        """
        if self.start == None:
            print('List is empty')
            return
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


    def insert_at_start(self,data: int):
        """
        Insert data at the start node
        
        Args:
            data: Value we want to insert into Linked List
        """
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node
            
    
    def insert_at_end(self,data: int):
        """
        Insert data at the end node
        
        Args:
            data: Value we want to insert into Linked List
        """
        new_node = Node(data)
        if self.start == None:
            self.start = new_node
            return
        current = self.start
        
        while current.next is not None:
            current = current.next
        current.next = new_node            
            
    
    def insert_after_value(self, x: int, data: int):
        """
        Insert new node after existing node
        
        Args:
            x: Existing value, after which we want to insert new value
            data: New value we want to insert
        """
        current = self.start
        print(current.next)
        
        while current is not None:
            if current.value == x:
                break
            current = current.next

        if current is None:
            print('Value not in the list')
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            
    
    def insert_before_value(self, x: int, data: int):
        """
        Insert new value before the existing one
        
        Args:
            x: Existing value
            data: New value we want to insert
        """
        if self.start == None:
            return
        
        if x == self.start.value:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node
            return

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
                    
    
    def insert_at_index(self, index: int, data: int):
        """
        Insert new value at a specific index
        
        Args:
            index: Index location
            data: New value to insert
        """
        if index == 1:
            new_node = Node(data)
            new_node.next = self.start
            self.start = new_node
        
        i = 1
        current = self.start
        
        while i < index -1 and current is not None:
            current = current.next
            i = i + 1
        if current is None:
            print('Index Out of Bound')
        else:
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
                    


"""
So far, so good. Let test our linked list class and method we implemented

"""


# Initialize empty linked list

linkedlist = LinkedList()


# Insert new node at the start
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




