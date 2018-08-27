# ------------------------------
# 166. Fraction to Recurring Decimal
# 
# Description:
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# Version: 1.0
# 08/26/18 by Jianfa
# ------------------------------

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        res = []
        res.append('-' if (numerator > 0) ^ (denominator > 0) else "")
        
        num = abs(numerator)
        denom = abs(denominator)
        
        # Integral part
        res.append(str(num / denom))
        num %= denom
        if num == 0:
            return ''.join(res)
        
        res.append('.')
        dic = dict()
        dic[num] = len(res)
        # Fractional part
        while num:
            num *= 10
            res.append(str(num / denom))
            num %= denom
            if num in dic: # fractional part is start to repeat
                res.insert(dic[num], '(')
                res.insert(len(res), ')')
                break
            else:
                dic[num] = len(res)
            
        return ''.join(res)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get solution from https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51106/My-clean-Java-solution
# The point is to seperate building the result to integral part and fractional part.
# Maintain a list, add digits to the list one by one.