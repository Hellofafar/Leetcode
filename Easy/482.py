# ------------------------------
# 482. License Key Formatting
# 
# Description:
# 
# Version: 2.0
# 10/07/18 by Jianfa
# ------------------------------

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""
         
        alphaStr = ''.join(S.split('-')).upper()
        count = len(alphaStr)  # Count the number of alphanumerical characters
        if count <= K:  # Number of characters is less than K
            return alphaStr
        
        firstSize = count % K  # Get the size of first group. If firstSize is 0, size of firstGroup is K
        if firstSize == 0:
            firstSize = K
            
        res = alphaStr[:firstSize]  # res is the string to return, get the first group of characters at first
        i = firstSize
        while i < count:            # For following groups, every time append "-" and characters to res
            res += '-{}'.format(alphaStr[i:i+K])
            i += K
        
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Find a very smart solution: https://leetcode.com/problems/license-key-formatting/discuss/96512/Java-5-lines-clean-solution
# public String licenseKeyFormatting(String s, int k) {
#     StringBuilder sb = new StringBuilder();
#     for (int i = s.length() - 1; i >= 0; i--)
#         if (s.charAt(i) != '-')
#             sb.append(sb.length() % (k + 1) == k ? '-' : "").append(s.charAt(i));
#     return sb.reverse().toString().toUpperCase();
# } 
# 
# Very smart: sb.length() % (k + 1) == k ? '-' : ""