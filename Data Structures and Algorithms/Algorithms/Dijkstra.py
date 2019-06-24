"""
Created on Mon Jun 24 2019

@author: Nodar Okroshiashvili
"""




"""

Dijkstra' Shortest Path Algorithm

"""



import sys
import heapq


class Edge:
    
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        


class Node:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.min_distance = sys.maxsize
        
        
    def __cmp__(self, other_vertex):
        return self.cmp(self.min_distance, other_vertex.min_distance)
    
    def __lt__(self, other):
        selfPriority = self.min_distance
        otherPriority = other.min_distance
        return selfPriority < otherPriority
    

class Dijkstra:
    
    def Calculate_Shortest_Path(self, vertex_list, star_vertex):
        
        q = []
        star_vertex.min_distance = 0
        heapq.heappush(q, star_vertex)
        
        while q:
            
            actual_vertex = heapq.heappop(q)
            
            for edge in actual_vertex.adjacencyList:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight
                
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(q, v)
    
    def Get_Shortest_Path(self, target_vertex):
        print('Shortest path to vertex is: ', target_vertex.min_distance)
        
        node = target_vertex
        
        while node is not None:
            print('%s' % node.name)
            node = node.predecessor
    




# Test the algorithm

# Create the nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")


# Create the edges, which consist of weight, starting vertex and target vertex
edge1 = Edge(5,node1,node2)
edge2 = Edge(8,node1,node8)
edge3 = Edge(9,node1,node5)
edge4 = Edge(15,node2,node4)
edge5 = Edge(12,node2,node3)
edge6 = Edge(4,node2,node8)
edge7 = Edge(7,node8,node3)
edge8 = Edge(6,node8,node6)
edge9 = Edge(5,node5,node8)
edge10 = Edge(4,node5,node6)
edge11 = Edge(20,node5,node7)
edge12 = Edge(1,node6,node3)
edge13 = Edge(13,node6,node7)
edge14 = Edge(3,node3,node4)
edge15 = Edge(11,node3,node7)
edge16 = Edge(9,node4,node7)


# Set the adjacency list
node1.adjacencyList.append(edge1)
node1.adjacencyList.append(edge2)
node1.adjacencyList.append(edge3)
node2.adjacencyList.append(edge4)
node2.adjacencyList.append(edge5)
node2.adjacencyList.append(edge6)
node8.adjacencyList.append(edge7)
node8.adjacencyList.append(edge8)
node5.adjacencyList.append(edge9)
node5.adjacencyList.append(edge10)
node5.adjacencyList.append(edge11)
node6.adjacencyList.append(edge12)
node6.adjacencyList.append(edge13)
node3.adjacencyList.append(edge14)
node3.adjacencyList.append(edge15)
node4.adjacencyList.append(edge16)


# Create vertex list
vertex_list = (node1,node2,node3, node4, node5, node6, node7, node8)


algorithm = Dijkstra()

algorithm.Calculate_Shortest_Path(vertex_list, node1)

# Calculate the shortest path from node A to node D
algorithm.Get_Shortest_Path(node4)




