# ------------------------------
# 917. Reverse Only Letters
# 
# Description:
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
# 
# Example 1:
# Input: "ab-cd"
# Output: "dc-ba"
# 
# Example 2:
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# Example 3:
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# Note:
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        start = 0
        end = len(S) - 1
        chars = list(S)
        while start < end:
            if not chars[start].isalpha():
                start += 1
            elif not chars[end].isalpha():
                end -= 1
            else:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1
        
        return "".join(chars)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointers solution, swap the characters if both are letters.
# 
# O(N) time O(N) space