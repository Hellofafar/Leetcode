# ------------------------------
# Implement Trie (Prefix Tree)
# 
# Description:
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# Note:
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# Version: 2.0
# 11/14/19 by Jianfa
# ------------------------------

class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.isWord = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            index = ord(c) - 97
            if p.chars[index] is None:
                p.chars[index] = TrieNode()
            p = p.chars[index]
        p.isWord = True
        
    
    def searchPrefix(self, prefix: str) -> TrieNode:
        p = self.root
        for c in prefix:
            index = ord(c) - 97
            if p.chars[index] is not None:
                p = p.chars[index]
            else:
                return None
        return p
    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.searchPrefix(word)
        # if p is None, it will be False
        return p is not None and p.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.searchPrefix(prefix) is not None        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Python solution. TrieNode idea borrowed from problem 212.