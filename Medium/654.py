# ------------------------------
# 654. Maximum Binary Tree
# 
# Description:
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
# 
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
# 
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
# 
#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1
# 
# Note:
# The size of the given array will be in the range [1,1000].
# 
# Version: 1.0
# 12/22/18 by Jianfa
# ------------------------------

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(nums, 0, len(nums))
    
    def constructTree(self, nums, l, r):
        if l == r:
            return None
                
        max_idx = self.findmax(nums, l, r)
        
        root = TreeNode(nums[max_idx])
        root.left = self.constructTree(nums, l, max_idx)
        root.right = self.constructTree(nums, max_idx + 1, r)
        
        return root
        
    def findmax(self, nums, l, r):
        max_i = l

        for i in range(l, r):
            if nums[i] > nums[max_i]:
                max_i = i

        return max_i

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution from Solution section.
# 
# The algorithm consists of the following steps:
# 
# 1.Start with the function call construct(nums, 0, n). Here, n refers to the number of elements in the given numsnums array.
# 2. Find the index, max_i, of the largest element in the current range of indices (l:r-1). Make this largest element, nums[max_i] as the local root node.
# 3. Determine the left child using construct(nums, l, max_i). Doing this recursively finds the largest element in the subarray left to the current largest element.
# 4. Similarly, determine the right child using construct(nums, max_i + 1, r).
# 5. Return the root node to the calling function.