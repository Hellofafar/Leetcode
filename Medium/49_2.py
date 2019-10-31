# ------------------------------
# 49. Group Anagrams
# 
# Description:
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# Version: 2.0
# 10/19/19 by Jianfa
# ------------------------------

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans["".join(sorted(s))].append(s)
        return ans.values()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# More consice sorted solution.
#
# O(NK * logK) time, N is the length of strs, K is the maximum length of a string in strs
# O(NK) space