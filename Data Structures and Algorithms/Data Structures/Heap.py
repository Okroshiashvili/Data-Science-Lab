


"""
Heaps are the most efficient implementation of priority queues.

Heaps are basically binary tree. There are two main binary heaps:
min heap and max heap.
    
In min heap, root node is always less or equal to its child or children
and in max heap root node is always greater than or equal to its children.


"""


class Heap:
    
    # The number of items in the Heap
    HEAP_SIZE = 10
    
    
    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.currentPosition = -1
        

    def IsFull(self):
        """
        Checks if heap capacity is full
        
        Returns:
            True or False
        """
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False
        
    
    def Insert(self, item: int):
        """
        Insert new value into a heap
        
        Args:
            item: The value to insert
        """
        if self.IsFull():
            print('Heap is full...')
            return
        
        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.FixUp(self.currentPosition)
        

    def FixUp(self, index):
        """
        This function makes sure there is no violation in the heap
        """
        parentIndex = int((index - 1)/2)
        
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = (int((6 - 1) / 2))
            
    
    def heapsort(self):
        """
        Sorts the heap
        """
        for i in range(0, self.currentPosition + 1):
            temp = self.heap[0]
            print('%d ' % temp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = temp
            self.FixDown(0, self.currentPosition - i - 1)
            
    def FixDown(self, index, upto):
        """
        This function makes sure there is no violation in the heap        
        """
        
        while index <= upto:
            
            leftchild = 2 * index + 1
            rightchild = 2 * index + 2
            
            if leftchild < upto:
                childToSwap = None
                
                if rightchild > upto:
                    childToSwap = leftchild
                else:
                    if self.heap[leftchild] > self.heap[rightchild]:
                        childToSwap = leftchild
                    else:
                        childToSwap = rightchild
                        
                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                index = childToSwap
            else:
                break
                    


# Test our algorithm

heap = Heap()

heap.Insert(10)
heap.Insert(-20)
heap.Insert(0)
heap.Insert(2)
heap.Insert(4)
heap.Insert(5)
heap.Insert(6)
heap.Insert(7)
heap.Insert(20)
heap.Insert(15)

heap.IsFull()


heap.heapsort()

