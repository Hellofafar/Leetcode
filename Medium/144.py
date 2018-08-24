# ------------------------------
# 144. Binary Tree Preorder Traversal
# 
# Description:
# Given a binary tree, return the preorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,2,3]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
# Version: 1.0
# 08/23/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        traverse = [root]
        while traverse:
            node = traverse.pop()
            res.append(node.val)
            if node.right:
                traverse.append(node.right)
            if node.left:
                traverse.append(node.left)
        
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Iterative solution.
# Maintain a traverse list to decide the visiting order of nodes.