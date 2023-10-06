class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return sum(ord(char) for char in str(key)) % self.size
    
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
    

def remove_duplicates(input_list):
    unique_elements = HashTable(size=100)
    result = []

    for item in input_list:
        if unique_elements.get(item) is None:
            unique_elements.insert(item, True)
            result.append(item)

    return result

input_list = [1, 2, 3, 4, 3, 2, 6, 8, 6, 10]

print(remove_duplicates(input_list))
