class Trie(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix):
        node = self
        for ch in prefix:
            index = ord(ch) - ord("a")
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def insert(self, word):
        node = self
        for ch in word:
            index = ord(ch) - ord("a")
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        return self.searchPrefix(prefix) is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
