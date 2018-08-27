# ------------------------------
# 165. Compare Version Numbers
# 
# Description:
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
# 
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
# 
# Example 1:
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# 
# Example 2:
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# 
# Example 3:
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
# 
# Version: 1.0
# 08/26/18 by Jianfa
# ------------------------------

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        i = 0
        while i < min(len(v1), len(v2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1
        
        if len(v1) > len(v2): # There may be example like 1.0.0 vs 1
            temp = [int(x) for x in v1[i:] if int(x) != 0]
            if temp:
                return 1
            else:
                return 0
        
        elif len(v1) < len(v2): # 1 vs 1.0.0
            temp = [int(x) for x in v2[i:] if int(x) != 0]
            if temp:
                return -1
            else:
                return 0
        
        else:
            return 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Split by '.' at first and compare each of elements.