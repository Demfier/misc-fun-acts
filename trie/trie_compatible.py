# Python program for insert and search
# operation in a Trie


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return [[[], [], [], []], False]

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return int(ch)

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl[0][index]:
                pCrawl[0][index] = self.getNode()
            pCrawl = pCrawl[0][index]

        # mark last node as leaf
        pCrawl[1] = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl[0][index]:
                return False
            pCrawl = pCrawl[0][index]

        return pCrawl is not None and pCrawl[1]


# driver function
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["2201", "0", "110", "1201"]
    output = ["Not present in trie", "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("2", output[t.search("2")]))
    print("{} ---- {}".format("2201", output[t.search("2201")]))
    print("{} ---- {}".format("1321", output[t.search("1321")]))
    print("{} ---- {}".format("0", output[t.search("0")]))


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)
