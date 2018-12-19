# ------------------------------
# 337. House Robber III
# 
# Description:
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
# 
# Example 1:
# Input: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# 
# Example 2:
# Input: [3,4,5,1,3,null,1]
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
# 
# Version: 1.0
# 12/18/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robSub(root)
        return max(res)
    
    def robSub(self, root):
        if not root:
            return [0, 0]
        
        left = self.robSub(root.left)
        right = self.robSub(root.right)
        res = [0, 0]  # First element is maximum value when root is not robbed, second element is maximum value when root is robbed
        
        res[0] = max(left) + max(right)  # Maximum value from left plus maximum value from right
        res[1] = left[0] + right[0] + root.val  # Root is robbed, left and right child cannot be robbed
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Great idea from https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem