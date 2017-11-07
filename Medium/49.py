# ------------------------------
# 49. Group Anagrams
# 
# Given an array of strings, group anagrams together.
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        candidates = {}
        for word in strs:
            if tuple(sorted(word)) not in candidates:
                candidates[tuple(sorted(word))] = [word]
            else:
                candidates[tuple(sorted(word))].append(word)
        
        anagrams = []
        for key in candidates:
            anagrams.append(candidates[key])
        
        return anagrams

if __name__ == "__main__":
    test = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(test.groupAnagrams(strs))

# ------------------------------
# Summary:
# Use sorted letter set as key, remember to sorted the word at first. So that can avoid the situation that two
# words have same letters but different count, e.g. hop and pooh.
# Very concise solution from Solution section:
# ans = collections.defaultdict(list)
# for s in strs:
#   ans[tuple(sorted(s))].append(s)
# return ans.values()