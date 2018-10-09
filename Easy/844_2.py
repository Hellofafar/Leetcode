# ------------------------------
# 844. Backspace String Compare
# 
# Description:
# 
# Version: 2.0
# 10/07/18 by Jianfa
# ------------------------------

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S) - 1
        j = len(T) - 1
        
        Sskip = 0
        Tskip = 0
        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == '#':
                    Sskip += 1
                    i -= 1
                elif Sskip > 0:
                    Sskip -= 1
                    i -= 1
                else:
                    break
                    
            while j >= 0:
                if T[j] == '#':
                    Tskip += 1
                    j -= 1
                elif Tskip > 0:
                    Tskip -= 1
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            
            i -= 1
            j -= 1
            
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer solution from Solution section.