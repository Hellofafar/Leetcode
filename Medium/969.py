# ------------------------------
# 969. Pancake Sorting
# 
# Description:
# Given an array A, we can perform a pancake flip: We choose some positive integer 
# k <= A.length, then reverse the order of the first k elements of A.  We want to perform 
# zero or more pancake flips (doing them one after another in succession) to sort the array A.
# 
# Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid 
# answer that sorts the array within 10 * A.length flips will be judged as correct.
# 
# Example 1:
# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k=4): A = [1, 4, 2, 3]
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
# 
# Example 2:
# Input: [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.
# 
# Note:
# 1 <= A.length <= 100
# A[i] is a permutation of [1, 2, ..., A.length]
# 
# Version: 1.0
# 11/03/19 by Jianfa
# ------------------------------

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        # A is a permutation of [1, 2, ..., A.length]
        for x in range(len(A),1,-1):
            i = A.index(x)  # find index of next maximum
            res.append(i+1) # reverse first i + 1 elements to make x be the first
            res.append(x)   # reverse x elements to make x be the last
            A = A[:i:-1] + A[:i] # get the new A without x after two reverse
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/pancake-sorting/discuss/214213/JavaC%2B%2BPython-Straight-Forward
# Find the index i of the next maximum number x.
# Reverse i + 1 numbers, so that the x will be at A[0]
# Reverse x numbers, so that x will be at A[x - 1].
# Repeat this process N times.
# 
# In the for loop, search the next maximum based on descending order of A
# 
# O(N^2) time, O(1) space