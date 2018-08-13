# ------------------------------
# 113. Path Sum II
# 
# Description:
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# 
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# 
# Version: 1.0
# 08/12/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        curlist = []
        self.helper(res, curlist, root, sum)
        return res
    
    def helper(self, res, curlist, root, sum):
        if not root:
            return
            
        curlist.append(root.val)
        if sum == root.val and not root.left and not root.right:
            temp = [x for x in curlist]
            res.append(temp)
            curlist.pop()
            return
        
        else:
            self.helper(res, curlist, root.left, sum - root.val)
            self.helper(res, curlist, root.right, sum - root.val)
        
        curlist.pop()

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Notice the number may be negative integer.