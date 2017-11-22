# ------------------------------
# 58. Length of Last Word
# 
# Description:
# vGiven a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length 
# of last word in the string.
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space characters only.
# Example:
# Input: "Hello World"
# Output: 5
# 
# Version: 1.0
# 11/21/17 by Jianfa
# ------------------------------

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split(' ')

        for w in words[::-1]:
            if len(w) > 0:
                return len(w)
        return 0

# Used for testing
if __name__ == "__main__":
    test = Solution()
    s = "world "

    print(test.lengthOfLastWord(s))

# ------------------------------
# Summary:
# Note that the string may leave space at the end.