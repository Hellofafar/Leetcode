# ------------------------------
# 117. Populating Next Right Pointers in Each Node II
# 
# Description:
# Given a binary tree
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Note:
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# 
# Example:
# Given the following binary tree,
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# 
# After calling your function, the tree should look like:
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL
# 
# Version: 1.0
# 08/14/18 by Jianfa
# ------------------------------

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            prev = TreeLinkNode(0)
            curr = prev
            while root:
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                
                root = root.next

            root = prev.next

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 