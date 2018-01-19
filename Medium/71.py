# ------------------------------
# 71. Simplify Path
# 
# Description:
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# Version: 1.0
# 01/18/18 by Jianfa
# ------------------------------

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return path
        
        directory = path.split('/')
        stack = []
        
        for d in directory:
            if d == "..":
                if not stack:
                    pass
                else:
                    stack.pop()
            
            elif d != "." and d != "":
                stack.append(d)
            
        if not stack:
            return "/"
        
        else:
            return "/" + "/".join(stack)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Stack solution.
# Think about the edge case. When there are multiple "..", consider "/".