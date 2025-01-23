class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.is_end_word = False

class buildTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.words.append(word)
            node.words.sort()
        node.is_end_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.is_end_word
    

bt = buildTrie()
list = ['apple','appy','king','kin']
for name in list:
    bt.insert(name)
print(bt.search('apple'))



