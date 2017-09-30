# ------------------------------
# 9. Palindrome Number
# 
# Description:
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# Version: 1.0
# 09/29/17 by Jianfa
# ------------------------------

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        else:
            reverse_num = 0
            while x > reverse_num:
                reverse_num = reverse_num * 10 + x % 10
                x = x // 10
            
            return x == reverse_num or x == reverse_num // 10
    

# Used for test
if __name__ == "__main__":
    test = Solution()
    x = 0
    
    print(test.isPalindrome(x)) 

# Summary
# I borrowed the idea from solution page: https://leetcode.com/problems/palindrome-number/solution/
# Reverse last half of the integer and compare first half and second half og number to check if they are same.
# The other idea from other solution is converting number into string. It seems the system accept this solution,
# although extra space is not allowed according to description.
# e.g. a = str(x).strip()
#      if a == a[::-1]:
#          return True