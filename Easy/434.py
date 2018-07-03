# ------------------------------
# 434. Number of Segments in a String
# 
# Description:
# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
# Please note that the string does not contain any non-printable characters.
# Example:
# Input: "Hello, my name is John"
# Output: 5
# 
# Version: 1.0
# 07/02/18 by Jianfa
# ------------------------------

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Difference between s.split() and s.split(' '):
# ''.split() = []
# ''.split(' ') = ['']