# ------------------------------
# 187. Repeated DNA Sequences
# 
# Description:
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit 
# comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# Version: 1.0
# 10/06/17 by Jianfa
# ------------------------------

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_len = len(s)
        s_dict = {}
        res = set()
        for i in range(s_len - 9):
            if s[i:i+10] in s_dict:
                res.add(s[i:i+10])
            else:
                s_dict[s[i:i+10]] = 1
        
        return list(set(res))


# Used for test
if __name__ == "__main__":
    test = Solution()
    s = "AAAAAAAAAAA"

    res = test.addTwoNumbers(a4, b3)
    print(test.findRepeatedDnaSequences(s))

# ------------------------------
# Summary:
# O(n) solution with O(n) space.
# Key idea is to use set/dict to detect whether the string appears has appeared.
# Another idea for saving space is to use int in replace of string. e.g. Let A for 1, C for 2, G for 3, T for 4.
# Then a ten-unit string can be converted to a 10-digit integer and save the space. May use a large array to
# imitate a hash map.