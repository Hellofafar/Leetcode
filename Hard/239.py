# ------------------------------
# 239. Sliding Window Maximum
# 
# Description:
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
# Example:
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
# Follow up:
# Could you solve it in linear time?
# 
# Version: 1.0
# 09/23/18 by Jianfa
# ------------------------------

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        deque = []
        res = []
        
        for i in range(len(nums)):
            while deque and deque[0] < i - k + 1:  # The first index in deque is out of bound of window
                deque.pop(0)
            
            while deque and nums[deque[-1]] <= nums[i]:  # The number matched last index is less than nums[i], its index should be removed since it will never be a max value
                deque.pop()
                
            deque.append(i)
            if i >= k - 1:  # For the first k-1 element, no max value will be outputted because window size is k
                res.append(nums[deque[0]])
        
        return res
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from https://www.youtube.com/watch?v=ShbRCjvB_yQ and https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation