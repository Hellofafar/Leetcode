# ------------------------------
# 340. Longest Substring with At Most K Distinct Characters
# 
# Description:
# Given a string, find the length of the longest substring T that contains at most k distinct characters.
# For example, Given s = “eceba” and k = 2,
# T is "ece" which its length is 3.
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_dict = {}
        lowest = 0
        res = 0
        
        for i, char in enumerate(s):
            char_dict[char] = i
            if len(char_dict) > k:
                lowest = min(char_dict.values())
                del char_dict[s[lowest]]
                lowest += 1
            res = max(i - lowest + 1, res)
        
        return res

if __name__ == "__main__":
    test = Solution()
    s = "eceba"
    k = 2

    print(test.lengthOfLongestSubstringKDistinct(s, k))

# ------------------------------
# Summary:
# Use hash table to serve as a sliding window.
# The idea is from the discuss section.
# Because the values in d represents the rightmost location of each character in the sliding window, in order to 
# find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.