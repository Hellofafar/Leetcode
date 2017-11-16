# ------------------------------
# 345. Reverse Vowels of a String
# 
# Description:
# 
# Version: 1.0
# 11/15/17 by Jianfa
# ------------------------------

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        
        left = 0
        right = len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_list = list(s)
        while left < right:
            if s_list[left] not in vowels:
                left += 1
                continue
            
            if s_list[right] not in vowels:
                right -= 1
                continue
            
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        
        return "".join(s_list)

# ------------------------------
# Summary:
# Two pointer