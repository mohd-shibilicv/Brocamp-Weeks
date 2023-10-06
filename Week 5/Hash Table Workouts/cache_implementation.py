class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]
        return None
    

class Cache:
    def __init__(self, size):
        self.size = size
        self.cache_table = HashTable(size)

    def get_value(self, key):
        return self.cache_table.get(key)
    
    def set_value(self, key, value):
        self.cache_table.insert(key, value)


cache = Cache(size=5)

cache.set_value("name", "shibili cv")
cache.set_value("age", 20)
cache.set_value("score", 100)

print("Name :", cache.get_value("name"))
print("Age :", cache.get_value("age"))
print("Score :", cache.get_value("score"))
