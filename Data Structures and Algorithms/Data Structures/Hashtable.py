"""
Created on Tue Jun 18 2019

@author: Nodar Okroshiashvili
"""




"""

Hashtable is data structure that implements associative array abstract
data type.


Here, I implement simple Hashtable with linear probing to solve collision
problem.


Collision in hashtable is when hash function produces two identical keys
for two different values

"""



class HashTable:
    
    def __init__(self):
        self.size = 10 # Size of slots/buckets in hashtable
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    
    def put(self, key, data):
        # Inset method.
        # Inserts given data or values with given key
        
        index = self.hashfunction(key)
        
        # Not None implies there is a collision
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            
            # Rehash or try to find another empty slot/bucket
            index = (index + 1)%self.size
            
        # Make insertion
        self.keys[index] = key
        self.values[index] = data
        
    
    def get(self, key):
        # Get the value with given key
        
        index = self.hashfunction(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            
            index = (index + 1) % self.size
        
        # This means provided key is not in hashtable
        return None
    
    
    def hashfunction(self, key):
        # Returns hash value for given key
        
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % self.size
    

# Let test the algorithm

table = HashTable()

# Insert some data

table.put("apple",10)
table.put("orange",20)
table.put("car",30)
table.put("table",40)


print(table.get('table'))

print(table.get('cherry'))






