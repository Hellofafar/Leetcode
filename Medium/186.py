# ------------------------------
# 186. Reverse Words in a String II
# 
# Description:
# Given an input string , reverse the string word by word. 
# Example:
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# Note: 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# 
# Follow up: Could you do it in-place without allocating extra space? 
# Version: 1.0
# 11/03/18 by Jianfa
# ------------------------------

class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        start = 0
        for i in range(len(str)):
            if str[i] == ' ':  # Find a word before
                self.reverse(str, start, i-1)
                start = i + 1
        
        self.reverse(str, start, len(str) - 1)
        
    # Reverse s[start:end] (inclusive) of s
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from https://leetcode.com/problems/reverse-words-in-a-string-ii/discuss/53775/My-Java-solution-with-explanation
# Three step to reverse
# 1, reverse the whole sentence
# 2, reverse each word
# 3, reverse the last word, if there is only one word this will solve the corner case