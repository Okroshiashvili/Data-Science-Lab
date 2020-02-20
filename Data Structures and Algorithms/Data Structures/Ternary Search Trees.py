


"""

Ternary Search Trees

"""


class Node:
    
    def __init__(self, character):
        self.character = character
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None
        # Every node is associated with value 0 at the begining
        self.value = 0
        

class TST:
    
    def __init__(self):
        """
        Initialize the root node
        """
        self.rootNode = None


    def Insert_Item(self, node, key, value, index):
        c = key[index]
        
        if node == None:
            node = Node(c)
        
        if c < node.character:
            node.leftNode = self.Insert_Item(node.leftNode, key, value, index)
        elif c > node.character:
            node.rightNode = self.Insert_Item(node.rightNode, key, value, index)
        elif index < len(key) - 1:
            node.middleNode = self.Insert_Item(node.middleNode, key, value, index + 1)
        else:
            node.value = value
        return node


    def Get_Item(self, node, key, index):
        
        if node == None:
            return None
        
        c = key[index]
        
        if c < node.character:
            return self.Get_Item(node.leftNode, key, index)
        elif c > node.character:
            return self.Get_Item(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.Get_Item(node.middleNode, key, index + 1)
        else:
            return node
    

    def insert(self, key: str, value: int):
        """
        Takes key:value pair and inserts them in Tree
        
        Args:
            key: str value for a key
            value: int value for a value
        """
        self.rootNode = self.Insert_Item(self.rootNode, key, value, 0)
    
    
    def get(self, key: str) -> int:
        """
        Takes the key and returns its corresponding value
        
        Args:
            key: the key for which the value has to be returned
        
        Returns:
            int: value for a given key
        """
        node = self.Get_Item(self.rootNode, key, 0)
        
        if node == None:
            return -1
        
        return node.value
    




# Test the algorithm

tst = TST()


tst.insert('apple', 100)
tst.insert('orange', 200)

print(tst.get('orange'))




