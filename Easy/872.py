# ------------------------------
# 872. Leaf-Similar Trees
# 
# Description:
# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# 
# Note:
# Both of the given trees will have between 1 and 100 nodes.
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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        seq1 = []
        seq2 = []
        
        self.dfs(root1, seq1)
        self.dfs(root2, seq2)
        
        return seq1 == seq2
        
    def dfs(self, root, seq):
        if not root:
            return
        
        if not root.left and not root.right:
            seq.append(root.val)
            return
        
        self.dfs(root.left, seq)
        self.dfs(root.right, seq)
        return

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 