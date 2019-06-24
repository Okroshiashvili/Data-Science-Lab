"""
Created on Mon Jun 24 2019

@author: Nodar Okroshiashvili
"""




"""

Bellman-Ford Algorithm


Compared to Dijkstra's algorithm, Bellman-Forsd is slower but
Bellman-Ford algorithm can handle negative weights.

Dijkstra's algorithm choose edges gredely with the lowest cost:
Bellman-Ford relaxes all the adges at the same time for V-1 iteration.

Running time for Bellman-Ford is O(V*E)


"""




import sys


class Node:
    
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.min_distance = sys.maxsize
        

class Edge:
    
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
        


class Bellman_Ford:
    
    HAS_CYCLE = False
    
    def Calculate_Shortest_Path(self, vertex_list, edge_list, start_vertex):
        start_vertex.min_distance = 0
        
        for i in range(0, len(vertex_list) - 1):
            for edge in edge_list:
                
                u = edge.start_vertex
                v = edge.target_vertex
                
                new_distance = u.min_distance + edge.weight
                
                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.predecessor = u
                    
        for edge in edge_list:
            if self.has_cycle(edge):
                print('Negative cycle detected...')
                Bellman_Ford.HAS_CYCLE = True
                return
    
    def has_cycle(self, edge):
        if (edge.start_vertex.min_distance + edge.weight) < edge.target_vertex.min_distance:
            return True
        else:
            return False
    
    def Get_Shortest_Path(self, target_vertex):
        
        if not Bellman_Ford.HAS_CYCLE:
            print('Shortest path exist with the values: ', target_vertex.min_distance)
            
            node = target_vertex
            
            while node is not None:
                print('%s' % node.name)
                node = node.predecessor
            else:
                print('Negative cycle detected...')
            

# Test the algorithm
                
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")




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
edge17 = Edge(1,node1,node2)
edge18 = Edge(1,node2,node3)
edge19 = Edge(-3,node3,node1)




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



vertexList = (node1,node2,node3, node4, node5, node6, node7, node8)

edgeList = (edge17, edge18, edge19)

algorithm = Bellman_Ford()

algorithm.Calculate_Shortest_Path(vertexList, edgeList, node1)

algorithm.Get_Shortest_Path(node7)




