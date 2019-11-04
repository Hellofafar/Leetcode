# ------------------------------
# 958. Check Completeness of a Binary Tree
# 
# Description:
# Given a binary tree, determine if it is a complete binary tree.
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, 
# and all nodes in the last level are as far left as possible. It can have between 1 and 
# 2h nodes inclusive at the last level h.
# 
# Example 1:
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and 
# {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# 
# Example 2:
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
# 
# Note:
# The tree will have between 1 and 100 nodes.
# 
# Version: 1.0
# 11/03/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        
        # give index to every node starting from 1
        # for node k, its left node's index is 2k, its right node index is 2k + 1
        queue = [(root, 1)]
        lastIndex = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr[1] != lastIndex + 1:
                    # if index is not continuous, it's not complete
                    return False
                lastIndex = curr[1]
                if curr[0].left:
                    queue.append((curr[0].left, 2 * lastIndex))
                if curr[0].right:
                    queue.append((curr[0].right, 2 * lastIndex + 1))
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution, give index to each node based on their parent's index.