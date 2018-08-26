# ------------------------------
# 151. Reverse Words in a String
# 
# Description:
# Given an input string, reverse the string word by word.
# 
# Example:  
# Input: "the sky is blue",
# Output: "blue is sky the".
# 
# Note:
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
# 
# Follow up: For C programmers, try to solve it in-place in O(1) space.
# 
# Version: 1.0
# 08/25/18 by Jianfa
# ------------------------------

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        slist = s.split(' ')
        slist = [x for x in slist if x != '']
        if not slist:
            return ''
        slist.reverse()
        return ' '.join(slist)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Seems not to be a good solution for other language.