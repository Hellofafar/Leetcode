# ------------------------------
# 953. Verifying an Alien Dictionary
# 
# Description:
# In an alien language, surprisingly they also use english lowercase letters, but possibly 
# in a different order. The order of the alphabet is some permutation of lowercase letters.
# 
# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographicaly in this alien 
# language.
# 
# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# 
# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# 
# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
# 
# Note:
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

class Solution:
    mapping = {}
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i, c in enumerate(order):
            # map the character to order, e.g if it's "xy...", then mapping['x'] = 0, mapping['y'] = 1
            self.mapping[c] = i
        
        for i in range(1, len(words)):
            if self.isBigger(words[i-1], words[i]):
                return False
        
        return True
    
    # determine if str1 is bigger than str2
    def isBigger(self, str1, str2):
        m = len(str1)
        n = len(str2)
        i = 0
        while i < m and i < n:
            if str1[i] != str2[i]:
                # if the characters at index i are different, compare their values in mapping
                return self.mapping[str1[i]] > self.mapping[str2[i]]
            i += 1
        
        return m >= n

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Mapping solution from: https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order
# 
# O(NS) time, S is the max length of word
# O(1) space
# 
# Take advantage of python feature, an easier solution can be implemented with the help of
# comparing list.
# 
# Every word can be represented by a list of index of each characters
# e.g. if "app" -> [1,2,2], "apple" -> [1,2,2,3,4], we can get [1,2,2] < [1,2,2,3,4]
# In python list can be compared based on its value's lexicographical order.
# So use a list to store all words' index representation.
# 