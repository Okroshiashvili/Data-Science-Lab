


"""
Queue is a type of linear data structure, where data is connected one after
another in a form of queue. First element is queue is served first, while
last element is queue is served last.


When new element is added to the queue, it enters at the last position.
This process is called "enqueue".

When we need to remove element, the first element is deleted. This process
if called "dequeue".


"""


class Queue:

    def __init__(self,):
        # In the constructor there are three variables.
        
        # First is the list that will contain all the elements
        # So, we're useing list to make queue
        
        # Second is the first element of a list, to keep track of element index
        # The third variable is the last element which will keep track of the
        # last element of our queue
        
        self.queue = list()
        self.first = -1
        self.last = -1
        
    
    def enqueue(self, value: int):
        """
        Adds new value to the Queue

        Args:
            value: New value to add
        """
        if self.first == -1:
            self.first = self.first + 1
            
        self.last = self.last + 1
        self.queue.insert(self.last, value)
    

    def traverse(self):
        """
        Print the element of the queue
        """
        for i in self.queue:
            print(i)
        # Or uncomment below
        # return self.queue





# Initialize object
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)



queue.traverse()





# # Resources
# https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# https://dbader.org/blog/queues-in-python
# https://stackabuse.com/stacks-and-queues-in-python/


