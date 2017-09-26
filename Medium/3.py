# ------------------------------
# 3. Longest Substring Without Repeating Characters
# 
# Description:
# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# Version: 1.0
# 09/18/17 by Jianfa
# ------------------------------
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        i = 0
        sub_start = -1
        max_len = 0
        while i < len(s):
            if s[i] in pos:
                sub_start = max(sub_start, pos[s[i]])
                
            pos[s[i]] = i
            max_len = max(max_len, i - sub_start)
            i += 1

        return max_len


# Used for test
if __name__ == "__main__":
    test = Solution()
    string = "abba"
    
    print(test.lengthOfLongestSubstring(string))

# ------------------------------
# Summary:
# At first I use two variable "max_str" and "curr_str" to compare the length, but get Time Limit Exceeded.
# Finally I borrowed the idea from official solution: https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/