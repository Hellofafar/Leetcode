# ------------------------------
# 245. Shortest Word Distance III
# 
# Description:
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
# word1 and word2 may be the same and they represent two individual words in the list.
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
# Input: word1 = "makes", word2 = "makes"
# Output: 3
# 
# Note:
# You may assume word1 and word2 are both in the list.
# 
# Version: 1.0
# 11/04/18 by Jianfa
# ------------------------------

class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index = -1
        minDist = len(words)
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:  # If a word1 or word2 is found
                if index != -1 and (word1 == word2 or words[index] != words[i]):  # either word1 == word2 or current word is different from word[index]
                    minDist = min(minDist, i - index)
                
                index = i
        
        return minDist

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from https://leetcode.com/problems/shortest-word-distance-iii/discuss/67095/Short-Java-solution-10-lines-O(n)-modified-from-Shortest-Word-Distance-I
# Use an index to record last index of word1 or word2
# When next word1 or word2 is found, if word1 == word2 or current word is different from words[index]
# then get the distance and compare with minDist.