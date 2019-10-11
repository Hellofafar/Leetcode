# ------------------------------
# 423. Reconstruct Original Digits from English
# 
# Description:
# Given a non-empty string containing an out-of-order English representation of digits 
# 0-9, output the digits in ascending order.
# 
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That 
# means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# 
# Example 1:
# Input: "owoztneoer"
# Output: "012"
# 
# Example 2:
# Input: "fviefuro"
# Output: "45"
# 
# Version: 1.0
# 10/10/19 by Jianfa
# ------------------------------

from collections import defaultdict
class Solution:
    def originalDigits(self, s: str) -> str:
        if not s:
            return ""
        
        count = defaultdict(int)
        for c in s:
            if c == "z":
                count[0] += 1
            elif c == "w":
                count[2] += 1
            elif c == "u":
                count[4] += 1
            elif c == "x":
                count[6] += 1
            elif c == "g":
                count[8] += 1
            elif c == "o":
                count[1] += 1 # 1 - 0 - 2 - 4
            elif c == "h":
                count[3] += 1 # 3 - 8
            elif c == "f":
                count[5] += 1 # 5 - 4
            elif c == "s":
                count[7] += 1 # 7 - 6
            elif c == "i":
                count[9] += 1 # 9 - 5 - 6 - 8
            
        count[1] = count[1] - count[0] - count[2] - count[4]
        count[3] = count[3] - count[8]
        count[5] = count[5] - count[4]
        count[7] = count[7] - count[6]
        count[9] = count[9] - count[5] - count[6] - count[8]
        
        res = ""
        for i in range(10):
            res += str(i) * count[i]
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# zero: Only digit with z
# two: Only digit with w
# four: Only digit with u
# six: Only digit with x
# eight: Only digit with g