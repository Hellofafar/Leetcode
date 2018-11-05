# ------------------------------
# 244. Shortest Word Distance II
# 
# Description:
# Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
# 
# Version: 1.0
# 11/03/18 by Jianfa
# ------------------------------

import sys

class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.wordDict = {}
        for i, w in enumerate(words):
            if w in self.wordDict:
                self.wordDict[w].append(i)
            else:
                self.wordDict[w] = [i]
                

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = self.wordDict[word1]
        index2 = self.wordDict[word2]
        
        i = j = 0
        minDist = sys.maxsize
        while i < len(index1) and j < len(index2):
            idx1 = index1[i]
            idx2 = index2[j]
            if idx1 < idx2:
                minDist = min(minDist, idx2 - idx1)
                i += 1
            
            else:
                minDist = min(minDist, idx1 - idx2)
                j += 1
        
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use hash map to store indexs of every word in the list
# Use two pointer to check every index of word1, find the closest index in the word2 of it and compare the distance of them.