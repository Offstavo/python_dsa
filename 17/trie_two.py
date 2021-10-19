# Insertion on a trie data structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
        
# Time complexity of insertString is O(m)
# Space complexity of insertString is O(m)

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")

# code worked as expected