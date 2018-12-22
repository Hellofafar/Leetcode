# ------------------------------
# 513. Find Bottom Left Tree Value
# 
# Description:
# 
# Version: 2.0
# 12/21/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        children = [root]
        
        for node in children:
            if node.right:
                children.append(node.right)
            if node.left:
                children.append(node.left)
        
        return node.val

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Super smart right-to-left BFS solution from https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-+-Java)