# ------------------------------
# 257. Binary Tree Paths
# 
# Description:
# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
# 
# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
# Version: 1.0
# 06/23/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        res = []
        curr = []
        self.helper(res, curr, root)
        
        return res
        
    def helper(self, res, curr, node):
        curr.append(node.val)
        if not node.left and not node.right:
            temp = ""
            for i in range(len(curr) - 1):
                temp += str(curr[i]) + "->"
            temp += str(curr[-1])
            
            res.append(temp)
        
        if node.left:
            self.helper(res, curr, node.left)
        
        if node.right:
            self.helper(res, curr, node.right)
        
        curr.pop()


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution.