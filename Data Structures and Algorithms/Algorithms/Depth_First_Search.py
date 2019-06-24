"""
Created on Mon Jun 24 2019

@author: Nodar Okroshiashvili
"""




"""

Depth First Search

"""



class Node:
    
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None
        


class Depth_First_Search:
    
    def dfs(self, node):
        
        node.visited = True
        print("%s " % node.name)
        
        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)
    

# Test the algorithm
                
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")		
	
node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)	

dfs = Depth_First_Search()

dfs.dfs(node1)




