# ------------------------------
# 412. Fizz Buzz
# 
# Description:
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
# Example:
# n = 15,
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
# 
# Version: 1.0
# 07/02/18 by Jianfa
# ------------------------------

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                res.append('FizzBuzz')
            
            elif (i+1) % 3 == 0:
                res.append('Fizz')
                
            elif (i+1) % 5 == 0:
                res.append('Buzz')
                
            else:
                res.append(str(i+1))
        
        return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 