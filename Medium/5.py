# ------------------------------
# 5. Longest Palindromic Substring
# 
# Description:
# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
# 
# Examples:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
# Version: 1.0
# 09/28/17 by Jianfa
# ------------------------------
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

# Used for test
if __name__ == "__main__":
    test = Solution()
    string = "cbbd"
    
    print(test.longestPalindrome(string))

# ------------------------------
# Summary:
# I didn't solve this problem. I tried to convert the problem to longest common substring problem and 
# solve in n^2 time/space complexity, but met Time Limit Exceeded error, when input is "dddddd......".
# 
# I learned about this talented idea from one of top voted solution: 
# https://discuss.leetcode.com/topic/7144/python-o-n-2-method-with-some-optimization-88ms/2
# The idea is simple: when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2, 
# and that new maxPalindrome includes this new character.