# ------------------------------
# 616. Add Bold Tag in String
# 
# Description:
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap 
# the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by 
# only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need 
# to combine them.
# 
# Example 1:
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# 
# Example 2:
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
# 
# Version: 1.0
# 12/04/17 by Jianfa
# ------------------------------

import re

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not s:
            return s
        
        record = [0 for i in range(len(s))]
        for item in dict:
            if item in s:
                for m in re.finditer('(?=' + item + ')', s):
                    start = m.start()
                    end = start + len(item)  # I tried to use m.end() but it doesn't work for finditer()
                    for i in range(start, end):
                        record[i] = 1
        
        wrapping = False
        output = ""
        for idx, state in enumerate(record):
            if state:
                if not wrapping:
                    output += "<b>" + s[idx]
                    wrapping = True
                else:
                    output += s[idx]
            
            else:
                if wrapping:
                    output += "</b>" + s[idx]
                    wrapping = False
                else:
                    output += s[idx]
        
        if wrapping:
            output += "</b>"
        
        return output

# Used for testing
if __name__ == "__main__":
    test = Solution()


# ------------------------------
# Summary:
# I used re package from python, to get start and end index of a substring in overlapping situation.
# Then I defined a record list that to update the value to 1 if that position should be wrapped.