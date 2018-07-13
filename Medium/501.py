# ------------------------------
# 501. Find Mode in Binary Search Tree
# 
# Description:
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#    1
#     \
#      2
#     /
#    2
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
# 
# Version: 1.0
# 07/10/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}
        res = []
        
        def dfs(node):
            if not node:
                return
            
            count[node.val] = count.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if not count.values():
            return res
        
        maxCount = max(count.values())
        for i in count:
            if count[i] == maxCount:
                res.append(i)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Mainly based on idea from https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98104/Simple-Python-Explanation
# But I didn't solve the follow up with only O(1) space.