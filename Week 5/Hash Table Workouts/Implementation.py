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


hash_table = HashTable(10)

hash_table.insert("apple", 100)
hash_table.insert("orange", 200)
hash_table.insert("banana", 300)

print(hash_table.get("orange"))
print(hash_table.get("lemon"))
