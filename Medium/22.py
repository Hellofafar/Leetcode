# ------------------------------
# 22. Generate Parentheses
# 
# Description:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# 
# Version: 1.0
# 09/18/17 by Jianfa
# ------------------------------

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        elif n == 1:
            return ["()"]
        elif n == 2:
            return ["(())", "()()"]
        else:
            mid = n // 2
            temp_list = []

            for i in range(1, mid+1):
                temp1 = self.generateParenthesis(i)
                temp2 = self.generateParenthesis(n-i)
                for t1 in temp1:
                    for t2 in temp2:
                        if i == 1:
                            temp_list.append("(" + t2 + ")")
                        else:
                            pass
                        if t1 != t2:
                            temp_list.append(t1+t2)
                            temp_list.append(t2+t1)
                        else:
                            temp_list.append(t1+t2)                    

            return list(set(temp_list))


# Used for test
# if __name__ == "__main__":
#     test = Solution()
#     n = 4
    
#     print(test.generateParenthesis(n))

# ------------------------------
# Summary:
# At first I think there are only three combination: 
# ["("+generateParenthesis(n-1)+")", "()"+generateParenthesis(n-1), generateParenthesis(n-1)+"()"]
# But there is another situation. For example when n=4, there is a combination "(())(())", 
# which cannot fit in anyone I thought before.
# 
# It seems there is a general solution based on length of the rest:
# From sample 28 ms submission:
# 
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         def gen(s,l,r,res =[]):
#             if l:
#                 gen (s+'(', l-1, r, res)
#             if r > l:
#                 gen(s+')', l, r-1, res)
#             if not r:
#                 res += s,
#             return res
#         return gen('', n, n)