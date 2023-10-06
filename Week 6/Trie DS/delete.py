class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word

    def delete(self, word):
        if not self.root:
            return
        
        self._delete_recursive(self.root, word, 0)

    def _delete_recursive(self, node, word, index):
        if index == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
                if not node.children:
                    return True
            return False
        
        char = word[index]
        if char in node.children and self._delete_recursive(node.children[char], word, index + 1):
            del node.children[char]
            return not node.is_end_of_word and not node.children
        return False


trie = Trie()
trie.insert('apple')
trie.insert('app')

trie.delete('apple')

print(trie.search('apple')) # False
print(trie.search('app')) # True
