# ------------------------------
# 247. Strobogrammatic Number II
# 
# Description:
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
# 
# For example,
# Given n = 2, return ["11","69","88","96"].
# 
# Version: 1.0
# 12/10/17 by Jianfa
# ------------------------------

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        type1 = ["0", "1", "8"]
        type2 = ["6", "9"]
        nums = ["0", "1", "6", "8", "9"]
        
        
        if n == 0:
            return [""]
        
        elif n == 1:
            return ["0", "1", "8"]

        elif n == 2:
            return ["11", "69", "88", "96"]
        
        else:
            nums = [("1","1"), ("6","9"), ("8","8"), ("9","6")]
            res = []
            for item in nums:
                res.extend(self.helper(item, n-2))
                
            return res
            
        
    
    def helper(self, surrounding, n):
        res = []
        if n == 1:
            for x in ["0", "1", "8"]:
                res.append(x.join(surrounding))
            return res 
        
        elif n == 2:
            for x in ["00", "11", "69", "88", "96"]:
                res.append(x.join(surrounding))
            return res
        
        else:
            options = [("0","0"), ("1","1"), ("6","9"), ("8","8"), ("9","6")]
            for opt in options:
                temp_res = self.helper(opt, n - 2)
                for x in temp_res:
                    res.append(x.join(surrounding))
            return res
        

# Used for testing
if __name__ == "__main__":
    test = Solution()
    n = 5

    print(test.findStrobogrammatic(n))

# ------------------------------
# Summary:
# Recursion solution
# There are static start and ending so I use a helper function to solve it recursively. Note that at the
# very outside level, ("0","0") is not a valid start and ending pair.
# 
# There is a very simple solution, every time add a start and end character directly:
# def helper(p, q):
#     if p == 0: return ['']
#     if p == 1: return ['0', '1', '8']
#     mid, res = helper(p-2, q), []
#     for tmp in mid:
#         if p != q: res.append('0' + tmp + '0')
#         res.append('1' + tmp + '1')
#         res.append('6' + tmp + '9')
#         res.append('9' + tmp + '6')
#         res.append('8' + tmp + '8')
#     return res