


"""
Breadth First Search

"""


class Node:
    
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None



class Breadth_First_Search:
    
    def bfs(self, startNode):
        
        queue = []
        queue.append(startNode)
        startNode.visited = True
        
        # Breadth First Search is implemented by using Queue
        while queue:
            
            actualNode = queue.pop(0)
            print('%s ' % actualNode.name)
            
            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)
                    



# Test the algorithm


# insert nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

# Define neighbor nodes.node1 has children node2 and node3
node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)


bfs = Breadth_First_Search()

bfs.bfs(node1)



