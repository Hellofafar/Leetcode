# ------------------------------
# 482. License Key Formatting
# Now you are given a string S, which represents a software license key which we would like to format. 
# The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical 
# characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). 
# The dashes in the given string are possibly misplaced.
# 
# We want each group of characters to be of length K (except for possibly the first group, which could be 
# shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. 
# Additionally, all the lower case letters in the string must be converted to upper case.
# 
# So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need 
# to return the license key formatted according to the description above.
# 
# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
# Output: "24A0-R74K"
# Explanation: The string S has been split into two parts, each part has 4 characters.
# 
# Example 2:
# Input: S = "2-4A0r7-4k", K = 3
# Output: "24-A0R-74K"
# Explanation: The string S has been split into three parts, each part has 3 characters except the first part 
# as it could be shorter as said above.
# 
# Version: 1.0
# 11/04/17 by Jianfa
# ------------------------------

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp_str = S.split('-')
        dash_excluded = ""
        for item in temp_str:
            dash_excluded += item
            
        res = ""
        rest = len(dash_excluded) % K
        if rest > 0:
            res += dash_excluded[:rest]
            for i in range(len(dash_excluded))[rest::K]:
                res += "-" + dash_excluded[i:i+K]
        
        else:
            res += dash_excluded[:K]
            for i in range(len(dash_excluded))[K::K]:
                res += "-" + dash_excluded[i:i+K]
                
        return res.upper()

# Used for test
if __name__ == "__main__":
    test = Solution()
    S = "2-4A0r7-4k"
    K = 4

    print(test.licenseKeyFormatting(S, K))

# ------------------------------
# Summary:
# Exclude the dashes at first, then reform the sentence. Note the situation when length of string cannot be 
# devided by K.