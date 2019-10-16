# ------------------------------
# 457. Circular Array Loop
# 
# Description:
# You are given a circular array nums of positive and negative integers. If a number k at an 
# index is positive, then move forward k steps. Conversely, if it's negative (-k), move 
# backward k steps. Since the array is circular, you may assume that the last element's next 
# element is the first element, and the first element's previous element is the last element.
# 
# Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same 
# index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a 
# single direction. In other words, a cycle must not consist of both forward and backward movements.
# 
# Example 1:
# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
# 
# Example 2:
# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's 
# length is 1. By definition the cycle's length must be greater than 1.
# 
# Example 3:
# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement 
# from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward 
# movement. All movements in a cycle must follow a single direction.
# 
# Note:
# 
# -1000 ≤ nums[i] ≤ 1000
# nums[i] ≠ 0
# 1 ≤ nums.length ≤ 5000
# 
# Follow up:
# Could you solve it in O(n) time complexity and O(1) extra space complexity?
# 
# Version: 1.0
# 10/15/19 by Jianfa
# ------------------------------

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        if not nums:
            return False
            
        size = len(nums)
        def getIndex(i):
            return (i + nums[i]) % size
        
        for i in range(size):
            if nums[i] == 0:
                continue
            
            # slow and fast pointers
            slow = i
            fast = getIndex(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[getIndex(fast)] > 0:
                if slow == fast:
                    if slow == getIndex(slow):
                        # the loop with only one element
                        break
                    return True
                
                slow = getIndex(slow)
                fast = getIndex(getIndex(fast))
            
            # loop not found, set all elements along the way to 0
            slow = i
            val = nums[i]
            while nums[slow] * val > 0:
                nextIdx = getIndex(slow)
                nums[slow] = 0
                slow = nextIdx
            
        return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Slow/fast pointers solution from: https://leetcode.com/problems/circular-array-loop/discuss/94148/Java-SlowFast-Pointer-Solution
# 
# O(n) time and O(1) space