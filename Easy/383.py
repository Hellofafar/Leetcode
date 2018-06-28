# ------------------------------
# 383. Ransom Note
# 
# Description:
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
# Note:
# You may assume that both strings contain only lowercase letters.
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# Version: 1.0
# 06/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        
        ransomSet = set(ransomNote)
        magazineSet = set(magazine)
        
        for i in ransomSet:
            if ransomNote.count(i) > magazine.count(i):
                return False
        
        return True


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use set and compare the number of each character.