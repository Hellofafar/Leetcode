# ------------------------------
# 520. Detect Capital
# 
# Description:
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# Example 1:
# Input: "USA"
# Output: True
# 
# Example 2:
# Input: "FlaG"
# Output: False
# 
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
# 
# Version: 1.0
# 07/13/18 by Jianfa
# ------------------------------

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        pre = word[0]

        for i, c in enumerate(word[1:]):
            if i == 0:
                if ord(pre) >= 97 and ord(c) <= 90:
                    return False
            
            else:
                if ord(pre) >= 97 and ord(c) <= 90 or ord(pre) <= 90 and ord(c) >= 97:
                    return False
            
            pre = c
            
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I leverage the relation between every neighbour pair of letters. Analysis of relation is as follows:
# If it's 'aA', false;
# if it's 'AA', true;
# if it's 'aa', true;
# if it's 'Aa', when A is the first letter, true, otherwise false.