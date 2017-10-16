# ------------------------------
# 17. Letter Combinations of a Phone Number
# 
# Description:
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# (png)
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]. 
# 
# Version: 1.0
# 10/16/17 by Jianfa
# ------------------------------

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],
                       5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],
                       8:['t','u','v'], 9:['w','x','y','z'], 0:[' '], 1:['*']}
        res = []
        if len(digits) > 1:
            first_digit = int(digits[0])
            sub_digits = digits[1:]
            for letter in letter_dict[first_digit]:
                res += [letter + sub_str for sub_str in self.letterCombinations(sub_digits)]
            return res
                
        elif len(digits) == 1:
            return letter_dict[int(digits)]
        
        else:
            return res

        
# Used for test
if __name__ == "__main__":
    test = Solution()
    digits = "201"
    
    print(test.letterCombinations(digits))

# Summary
# Use recursive method to do string combination. Start from the last digit, and recursively add a digit before
# the string generated from previous substrings.
# Note: 0 for " " and 1 for "*", which is specified in the description.
