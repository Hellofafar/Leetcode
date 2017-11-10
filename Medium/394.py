# ------------------------------
# 394. Decode String
# 
# Description:
# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated 
# exactly k times. Note that k is guaranteed to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those 
# repeat numbers, k. For example, there won't be input like 3a or 2[4].
# 
# Examples:
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# Version: 1.0
# 11/08/17 by Jianfa
# ------------------------------

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = []
        num = ""  # The number is string too, e.g. 10 or 100. Must read character completely then convert to an integer
        res = []
        res.append("")  # It's necessary to add an empty string at first, which is used to concatenate all the string finally 
        for char in s:
            if char.isdigit():
                num += char
            
            elif char == "[":
                nums.append(int(num))
                num = ""
                res.append("")
            
            elif char == "]":
                temp = res.pop()
                k = nums.pop()
                res[-1] += k * temp
            
            else:
                res[-1] += char
                
        return res[0]
        

# ------------------------------
# Summary:
# Use stack to store string, and set different action when meeting digit, "[", "]" and letters.