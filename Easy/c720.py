# ------------------------------
# c720. Longest Word in Dictionary
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

# If there is no answer, return the empty string.
# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# 
# Contest 57
# Version: 1.0
# 11/04/17 by Jianfa
# ------------------------------

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        candidates = []
        res = ""
        max_len = 0
        first_flag = True
        for item in words:
            if len(item) == 1:
                candidates.append(item)
                if first_flag:
                    res = item
                    max_len = 1
                    first_flag = False

            else: 
                if item[:-1] in candidates:
                    candidates.append(item)
                    if len(item) > max_len:
                        res = item
                        max_len = len(item)
        
        return res
        
# Used for test
if __name__ == "__main__":
    test = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]

    print(test.longestWord(words))