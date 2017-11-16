# ------------------------------
# 686. Repeated String Match
# 
# Description:
# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring 
# of it. If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a 
# substring of A repeated two times ("abcdabcd").
# 
# Version: 1.0
# 11/13/17 by Jianfa
# ------------------------------

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) >= len(B):
            if B in A:
                return 1
            
            elif B in A * 2:
                return 2
        
        elif A in B:
            times = len(B) / len(A)
            for i in range(times, times + 3):
                if B in A * i:
                    return i
        
        return -1

# ------------------------------
# Summary:
# Some trap here:
# A = "aa" B = "a"
# A = "ab" B = "ba"
# A = "abc" B = "ca"
# Divide the situation to two: len(A) >= len(B), len(A) < len(B) (A must be substring of B at second situation)