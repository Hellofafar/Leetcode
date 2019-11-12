# ------------------------------
# 17. Letter Combinations of a Phone Number
# 
# Description:
# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note 
# that 1 does not map to any letters.
# 
# Example:
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# 
# Version: 2.0
# 11/11/19 by Jianfa
# ------------------------------

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # digit to letter mapping
        letterDict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g', 'h', 'i'], '5':['j','k','l'],
                      '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res = []
        def backtrack(prev, index):
            # index is the current digit to check
            if index == len(digits):
                res.append(prev)
                return
            
            for c in letterDict[digits[index]]:
                # traverse every characters mapping to current digits[index]
                backtrack(prev + c, index + 1)
        
        backtrack("", 0)
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack solution, using index to denote which digit to check, rather then putting the
# substring as parameter to backtrack function.