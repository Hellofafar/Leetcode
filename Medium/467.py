# ------------------------------
# 467. Unique Substrings in Wraparound String
# 
# Description:
# Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", 
# so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

# Now we have another string p. Your job is to find out how many unique non-empty substrings of 
# p are present in s. In particular, your input is the string p and you need to output the number 
# of different non-empty substrings of p in the string s.

# Note: p consists of only lowercase English letters and the size of p might be over 10000.

# Example 1:
# Input: "a"
# Output: 1

# Explanation: Only the substring "a" of string "a" is in the string s.
# Example 2:
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string s.
# Example 3:
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the 
# string s.
# 
# Version: 1.0
# 10/16/19 by Jianfa
# ------------------------------

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) <= 1:
            return len(p)
        
        # stringDict store the following information
        # key = ending letter of the substring
        # value = number of longest substring ended with key letter
        preLetter = p[0]
        stringDict = {preLetter:1}
        size = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(preLetter)) % 26 != 1:
                size = 1
            
            else:
                size += 1
                
            if p[i] not in stringDict:
                stringDict[p[i]] = size
            else:
                stringDict[p[i]] = max(stringDict[p[i]], size)
            preLetter = p[i]
        
            
        return sum(stringDict[k] for k in stringDict)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95439/Concise-Java-solution-using-DP
# Main idea is the max number of unique substring ENDS with a letter equals to the length of 
# max contiguous substring ends with that letter. Example "abcd", the max number of unique 
# substring ends with 'd' is 4, apparently they are "abcd", "bcd", "cd" and "d"
# At first my idea is to check the substring STARTS with a letter, but it's not easy to update
# max number during traverse, because you don't have the exact number for the new letter to
# update.
# 
# O(n) time and O(n) space