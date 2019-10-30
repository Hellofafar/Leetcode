# ------------------------------
# 560. Subarray Sum Equals K
# 
# Description:
# Given an array of integers and an integer k, you need to find the total number of 
# continuous subarrays whose sum equals to k.
# 
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k 
# is [-1e7, 1e7].
# 
# Version: 1.0
# 10/29/19 by Jianfa
# ------------------------------

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = 0
        count = 0
        sumDict = {0: 1} # if there is a subarray whose sum is k, can get sumDict[0] = 1
        
        for n in nums:
            preSum += n
            if preSum - k in sumDict:
                # if there exists a sum of subarray nums[:i] that is preSum - k
                # then sum of subarray between current number and nums[i] is k
                count += sumDict[preSum - k]
            sumDict[preSum] = sumDict.get(preSum, 0) + 1
        
        return count

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/subarray-sum-equals-k/discuss/102106/Java-Solution-PreSum-%2B-HashMap
# I thought about the accumulated sum, but I didn't think about using the map to store
# previous accumulated sum, so that it helps to check if the difference between current 
# sum and a certain sum is k.