# ------------------------------
# 722. Remove Comments
# 
# Description:
# 
# Too long description. Check https://leetcode.com/problems/remove-comments/description/
# 
# Example 2:
# Input: 
# source = ["a/*comment", "line", "more_comment*/b"]
# Output: ["ab"]
# Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
# 
# Version: 1.0
# 09/14/18 by Jianfa
# ------------------------------

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inCommentBlock = False
        
        res = []
        for line in source:
            if not inCommentBlock:
                newline = []
            i = 0
            while i < len(line):
                if line[i:i+2] == '/*' and not inCommentBlock:
                    inCommentBlock = True
                    i += 1
                
                elif line[i:i+2] == '*/' and inCommentBlock:
                    inCommentBlock = False
                    i += 1
                
                elif line[i:i+2] == '//' and not inCommentBlock:
                    break
                
                elif not inCommentBlock:
                    newline.append(line[i])
                
                i += 1
                
            if newline and not inCommentBlock:
                res.append("".join(newline))
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Take care of the second example.
# e.g.
# a = 1; /* this
# is a comment */ b = 1;
# 
# will return
# a = 1; b = 1;