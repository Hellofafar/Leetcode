# ------------------------------
# 14. Longest Common Prefix
# 
# Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# Version: 1.0
# 09/16/17 by Jianfa
# ------------------------------

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ""
        i = 0
        while True:
            c = []
            for s in strs:
                try:
                    c.append(s[i])
                except IndexError as err:  # There is a string reach reach the length limit
                    return common          # The previous common result will be the final result
            
            char_set = set(c)
            if len(char_set) == 1:         # There is only one character at the same position for all strings
                common += list(char_set)[0]
                i += 1
            else:
                break
        
        return common

# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     strings = ["aa", "a"]
    
#     print(test.longestCommonPrefix(strings))