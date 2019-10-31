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
# Version: 3.0
# 10/19/19 by Jianfa
# ------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        group = collections.defaultdict(list)
        for s in strs:
            counter = collections.Counter(s)
            charCount = [0] * 26
            for c in counter:
                charCount[ord(c) - ord('a')] = counter[c]
            group[tuple(charCount)].append(s)
        
        return group.values()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Categorize by Count solution from: https://leetcode.com/problems/group-anagrams/solution/
# 
# O(NK) time, N is the length of strs, K is the maximum length of a string in strs
# O(NK) space