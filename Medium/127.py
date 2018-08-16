# ------------------------------
# 127. Word Ladder
# 
# Description:
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
# 
# Version: 1.0
# 08/15/18 by Jianfa
# ------------------------------

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)  # Before make it a set, I met time exceed error.
        wordDist = 1
        toVisit = [beginWord]
        while toVisit:
            for _ in range(len(toVisit)):
                word = toVisit.pop(0)
                if word == endWord:
                    return wordDist
                
                for i in range(len(word)):
                    for j in range(26):
                        temp = word[:i] + chr(97+j) + word[i+1:]
                        if temp in wordList:
                            toVisit.append(temp)
                            wordList.remove(temp)
                
            wordDist += 1
        
        return 0


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Key point is BFS solution.
# Not sure why make wordList a set is important, maybe because remove() is time costly for list.
# Follow idea from https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution