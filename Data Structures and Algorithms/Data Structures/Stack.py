"""
Created on Mon May  6 2019

@author: Nodar Okroshiashvili
"""



"""

Stack is a type of linear data structure, where data is organized on
top of each other in a form of a stack



First element in the stack is placed ath the bottom of the stack, second
element is placed on top of first element and this procedure continues for
other elements.


If we want to remove element from the stack, we have to remove top element.

To add element to the stack we use function named "push" and to remove
we use function called "pop".


"""






# Let implement stack


class Stack:
    
    def __init__(self):
        self.stack = list() # This is an empty stack
        
    # we use function called "push" to inser elements in stack
    def push(self, value): # value parameter is the value we want to insert
        self.stack.append(value) # append means to add value at the end of a list
        
    # To delete element we use function pop
    def pop(self):
        if len(self.stack) < 1:
            print('The stack is empty')
        else:
            self.stack.pop()
        
    # Stack traversal, or printing stack elements
    def traverse(self):
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



# Resources
https://dbader.org/blog/stacks-in-python
https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html



