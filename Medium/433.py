# ------------------------------
# 433. Minimum Genetic Mutation
# 
# Description:
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
# 
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where 
# ONE mutation is defined as ONE single character changed in the gene string.
# 
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
# 
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene 
# must be in the bank to make it a valid gene string.
# 
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum 
# number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
# 
# Note:
# 
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# 
# Example 1:
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# return: 1
#  
# Example 2:
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# return: 2
# 
# Example 3:
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# return: 3
# 
# Version: 1.0
# 10/11/19 by Jianfa
# ------------------------------

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        if start == end:
            return 0
        
        bankSet = set(bank)
        charSet = set(["A", "C", "G", "T"])
        
        visited = set([start])
        queue = [start]
        
        level = 0
        while queue:
            # Every time check all strings in the current layer
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if cur == end:
                    return level
                
                for j in range(8):
                    for c in charSet:
                        temp = cur[:j] + c + cur[j+1:]
                        if temp not in visited and temp in bankSet:
                            queue.append(temp)
                            visited.add(temp)
            
            level += 1
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution from: https://leetcode.com/problems/minimum-genetic-mutation/discuss/91484/Java-Solution-using-BFS