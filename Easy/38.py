# ------------------------------
# 35. Count and Say
# 
# Description:
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.
# 
# Example 1:
# Input: 1
# Output: "1"
# 
# Example 2:
# Input: 4
# Output: "1211"
# 
# Version: 1.0
# 09/26/17 by Jianfa
# ------------------------------

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        counts = {1:'1', 2:'11', 3:'21', 4:'1211', 5:'111221'}
        if n <= 5:
            return counts[n]
        else:
            last_string = self.countAndSay(n - 1)
            count = 0
            digit = ''
            current_string = ''
            for n in last_string:
                if n == digit:
                    count += 1
                elif count == 0:
                    digit = n
                    count += 1
                else:  # n != digit and count != 0, which means there is a new digit 
                    current_string += str(count) + str(digit)
                    digit = n
                    count = 1
            
            current_string += str(count) + str(digit)
            
            return current_string


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     n = 0
# 
#     print(test.countAndSay(n))


# ------------------------------
# Summary:
# My idea: When ask for nth string, count and say (n-1)th string at first, then return recursively.
# Good idea from other solution:
# Use iterative idea.
# If n == 1, just return "1"
# If n > 1, set str = '', count = 1, first_digit = '1',
# then generate the string for next integer, until reach given n.