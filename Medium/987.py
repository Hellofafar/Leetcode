# ------------------------------
# 987. Vertical Order Traversal of a Binary Tree
# 
# Description:
# Given a binary tree, return the vertical order traversal of its nodes values.
# 
# For each node at position (X, Y), its left and right children respectively will be at 
# positions (X-1, Y-1) and (X+1, Y-1).
# 
# Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line 
# touches some nodes, we report the values of the nodes in order from top to bottom 
# (decreasing Y coordinates).
# 
# If two nodes have the same position, then the value of the node that is reported first 
# is the value that is smaller.
# 
# Return an list of non-empty reports in order of X coordinate.  Every report will have a 
# list of values of nodes.
# 
# # Example 1:
# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
# 
# Example 2:
# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
# 
# Version: 1.0
# 10/19/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # seen is a dictionary storing {x: {y: [node]}}
        seen = collections.defaultdict(lambda: collections.defaultdict(list))
        
        def dfs(root, x, y):
            if root:
                seen[x][y].append(root)
                dfs(root.left, x - 1, y - 1)
                dfs(root.right, x + 1, y - 1)
        
        dfs(root, 0, 0)
        res = []
        for x in sorted(seen):
            pos = []
            # report the values by decreasing Y coordinates so reverse sort
            for y in sorted(seen[x], reverse=True):
                pos.extend(sorted(node.val for node in seen[x][y]))  # don't forget to sort by the node.val
            res.append(pos)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow idea from https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solution/
# Simple idea using dictionary to store location and traverse using DFS.