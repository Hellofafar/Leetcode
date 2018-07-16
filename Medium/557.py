# ------------------------------
# 557. Reverse Words in a String III
# 
# Description:
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
# 
# Version: 1.0
# 07/15/18 by Jianfa
# ------------------------------

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        senList = s.split(' ')
        for i, w in enumerate(senList):
            senList[i] = w[::-1]
            
        return ' '.join(senList)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 