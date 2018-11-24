# ------------------------------
# 642. Design Search Autocomplete System
# 
# Description:
# 
# Version: 1.0
# 11/18/18 by Jianfa
# ------------------------------

from operator import itemgetter, attrgetter

class AutocompleteSystem:
    
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = Trie()
        # build a trie
        for i in range(len(sentences)):
            self.insert(self.root, sentences[i], times[i])
        
        self.currSent = ""
    
    def convert(self, char):  # Convert character to index number
        return 26 if char == ' ' else ord(char) - ord('a')
    
    def insert(self, trie, s, times):  # Add a string s to trie
        for c in s:
            if trie.branches[self.convert(c)] is None:
                trie.branches[self.convert(c)] = Trie()
            trie = trie.branches[self.convert(c)]
        trie.times += times
    
    def lookup(self, trie, s):
        nodeList = []
        for c in s:
            if trie.branches[self.convert(c)] is None:
                return []
            trie = trie.branches[self.convert(c)]
        
        self.traverse(s, trie, nodeList)
        return nodeList
    
    def traverse(self, s, trie, nodeList):
        if trie.times > 0:
            nodeList.append(Node(s, trie.times))
        for i in range(26):
            if trie.branches[i] is not None:
                self.traverse(s + chr(97+i), trie.branches[i], nodeList)
        if trie.branches[26] is not None:
            self.traverse(s + ' ', trie.branches[26], nodeList)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c == '#':
            self.insert(self.root, self.currSent, 1)
            self.currSent = ""  # RESET the input sentence
        
        else:
            self.currSent += c
            retList = self.lookup(self.root, self.currSent)
            retList.sort(key=attrgetter('sentence'))  # Sort alphabetically first (actually is second sort key)
            retList.sort(key=attrgetter('times'), reverse=True)  # Then sort by times (actually is first sort key)
        
            for i in range(min(3, len(retList))):
                res.append(retList[i].sentence)
        
        return res
        
class Node:
    def __init__(self, st, t):
        self.sentence = st
        self.times = t
        
class Trie:
    def __init__(self):
        self.branches = [None] * 27
        self.times = 0

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Trie idea from https://leetcode.com/problems/design-search-autocomplete-system/solution/
# Meet TLE.