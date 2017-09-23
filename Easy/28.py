# ------------------------------
# 28. Implement strStr()
# 
# Description:
# Implement strStr().
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# Version: 1.0
# 09/23/17 by Jianfa
# ------------------------------

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0

        elif not haystack:
            return -1

        elif not needle:
            return 0
        
        else:
            len_haystack = len(haystack)
            len_needle = len(needle)
            if len_haystack < len_needle:
                return -1

            p0, ph, pn = 0, 0, 0
            flag = False
            while p0 < len_haystack:
                if haystack[p0] == needle[pn] and pn == len_needle - 1:
                    if pn == 0:
                        return p0
                    else:
                        return ph
                elif haystack[p0] == needle[pn] and pn == 0:
                    flag = True
                    ph = p0
                    pn += 1
                elif flag and haystack[p0] == needle[pn]:
                    pn += 1
                elif flag and haystack[p0] != needle[pn]:
                    pn = 0
                    p0 = ph
                    flag = False

                p0 += 1

            return -1


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     haystack = "mississippi"
#     needle = "issip"
    
#     print(test.strStr(haystack, needle))


# ------------------------------
# Summary:
# I used a very stupid comparison idea that I compared every character of two strings.
# However, two string can be compared by "stringA" == "stringB" !!!
# So, the simple and efficient idea is: compare every possible substring of haystack which
# is as long as needle by "haystack[i: i + len(needle)] == needle".
# 
# The following solution is a sample 28 ms submission on Leetcode (only 4 lines):
# for i in range(len(haystack)-len(needle)+1):
#     if haystack[i: i + len(needle)] == needle:
#         return i
# return -1