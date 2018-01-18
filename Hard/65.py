# ------------------------------
# 65. Valid Number
# 
# Description:
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements 
# up front before implementing one.
# 
# Version: 1.0
# 01/17/18 by Jianfa
# ------------------------------

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = False
        sign = False
        numBefore = False
        decPoint = False
        power =  False
        end = False
        last = ""
        for c in s:
            if not start:
                if c == "+" or c == "-":
                    start = True
                    sign = True
                    
                elif c == ".":
                    start = True
                    decPoint = True
                
                elif not c.isdigit() and c != " ":
                    return False
                    
                elif c.isdigit():
                    start = True
            
            else:
                if not end:
                    if c == ".":
                        if decPoint or power:
                            return False

                        else:
                            if last != "+" and last != "-":
                                numBefore = True
                            decPoint = True
                            
                    elif c == "e":
                        if power:
                            return False
                        if last != "." and not last.isdigit():
                            return False
                        if last == "." and not numBefore:
                            return False
                        power = True
                        lastIsPower = True

                    elif c == " ":
                        if last == "e" or last == "+" or last == "-" or (last == "." and not numBefore):
                            return False
                        end = True
                        
                    elif c == "+" or c == "-":
                        if last != "e":
                            return False
                    
                    elif not c.isdigit():
                        return False
                    
                else:
                    if c != " ":
                        return False
            
            last = c
        
        if not start or last == "e" or last == "+" or last == "-":
            return False
        
        if last == "." and not numBefore:
            return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The worst problem I ever met.