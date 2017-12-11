# ------------------------------
# 524. Longest Word in Dictionary through Deleting
# 
# Description:
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
# 
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# Version: 1.0
# 12/10/17 by Jianfa
# ------------------------------

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxLen = 0
        res = ""
        for word in d:
            if len(word) >= maxLen:
                # item = list(s)
                last_pos = -1
                isvalid = True
                for c in word:
                    if c not in s:
                        isvalid = False
                        break   
                    
                    pos = s[last_pos+1:].find(c)  # Don't forget the 1!
                    if pos == -1:
                        isvalid = False
                        break
                    
                    else:
                        last_pos = pos + last_pos + 1  # Don't forget the 1!
                
                if isvalid:
                    if len(word) > maxLen:
                        res = word
                        maxLen = len(word)
                    else:
                        res = word if word < res else res
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# There are several traps here.
# My basic idea is to check every word, and check if the character in a word appear incrementally in the s.
# Every time I record position for current character in the s, and start to search next character from the
# last position.
# At first I use list.index(), but str.find() is an easier solution for me and find is not supported in list.