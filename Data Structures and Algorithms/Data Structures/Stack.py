


"""

Stack is a type of linear data structure, where data is organized on
top of each other in a form of a stack



First element in the stack is placed at the bottom of the stack, second
element is placed on top of first element and this procedure continues for
other elements.


If we want to remove element from the stack, we have to remove top element.

To add element to the stack we use function named "push" and to remove
we use function called "pop".


"""




class Stack:
    
    def __init__(self):
        """
        Initialize empty stack
        """
        self.stack = list()
    

    def push(self, value: int):
        """
        Insert value into a stack
        
        Args:
            value: value to insert at the end
        """
        self.stack.append(value)


    def pop(self):
        """
        Remove element from the stack

        """
        if len(self.stack) < 1:
            print('The stack is empty')
        else:
            self.stack.pop()
    
    
    def traverse(self):
        """
        Print stack element
        """
        print(self.stack)




# LEt test our stack implementation
        
stack = Stack()

# Add elements
stack.push(10)
stack.push(20)
stack.push(30)


# Traverse stack
stack.traverse()


# Remove element
stack.pop()

# Again traverse stack
stack.traverse()



# # Resources
# https://dbader.org/blog/stacks-in-python

# https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html



