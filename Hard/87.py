# ------------------------------
# 87. Scramble String
# 
# Description:
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings 
# recursively.
# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
# 
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
# 
# Version: 1.0
# 01/28/18 by Jianfa
# ------------------------------

import collections
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        
        char_dict = collections.defaultdict(int)
        for c in s1:
            char_dict[c] += 1
        
        for c in s2:
            char_dict[c] -= 1
        
        for key in char_dict:
            if char_dict[key] != 0:
                return False
        
        length = len(s1)
        for i in range(1,length):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[0:i], s2[length-i:]) and self.isScramble(s1[i:], s2[0:length-i]):
                return True
        
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from: https://leetcode.com/problems/scramble-string/discuss/29392/.