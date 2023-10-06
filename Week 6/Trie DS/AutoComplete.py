class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class AutoComplete:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def _find_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)

        for char, child in node.children.items():
            words.extend(self._find_words(child, prefix + char))
        
        return words
    
    def suggest(self, prefix):
        node = self._find_node(prefix)
        if node is None:
            return []
        
        return self._find_words(node, prefix)


auto_complete = AutoComplete()

words = ["brototype", "crossroads", 'cross', "bro", "batman", "bat"]

for word in words:
    auto_complete.insert(word)

prefix = ""
suggestions = auto_complete.suggest(prefix)
print(f"Suggestion for {prefix}:")
print(suggestions)
