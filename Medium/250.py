# ------------------------------
# 250. Count Univalue Subtrees
# 
# Description:
# Given a binary tree, count the number of uni-value subtrees.
# 
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# Example :
# Input:  root = [5,1,5,5,5,null,5]
# 
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# Output: 4
# 
# Version: 1.0
# 11/05/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.num = 0
        
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.num
        
    def helper(self, root):
        if not root:
            return True
        
        left_sub = self.helper(root.left)
        right_sub = self.helper(root.right)
        
        if left_sub and right_sub \
                    and (not root.left or root.val == root.left.val) \
                    and (not root.right or root.val == root.right.val):
            self.num += 1
            return True
        
        else:
            return False
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use self.num to serve as a global variable, and use a helper function to decide whether
# a try is a univalue subtree.
# A univalue tree mush satisfy three conditions:
# 1. left tree is univalue subtree
# 2. right tree is univalue subtree
# 3. root.val = root.left.val = root.right.value (if not null)