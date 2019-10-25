class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.helper(temp, res, 0, nums)
        return res
    
    def helper(self, temp, res, index, nums):
        if len(temp) > 1:
            res.append(list(temp))
        
        seen = set()
        for i in range(index, len(nums)):
            n = nums[i]
            if n in seen:
                continue
            if len(temp) == 0 or n >= temp[-1]:
                seen.add(n)
                temp.append(n)
                self.helper(temp, res, index+1, nums)
                temp.pop()

solution = Solution()
nums = [4,6,7,7]
print(solution.findSubsequences(nums))