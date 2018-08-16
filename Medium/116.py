# ------------------------------
# 116. Populating Next Right Pointers in Each Node
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
# 
# Note:
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# 
# Example:
# Given the following perfect binary tree,
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL
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
    prev = None
    def connect(self, root):
        if not root:
            return
        
        stack = [root]
        while stack:
            temp = []
            for _ in range(len(stack)):
                cur = stack.pop(0)
                if len(stack) == 0:
                    cur.next = None
                
                else:
                    cur.next = stack[0]
                
                if cur.left:
                    temp.append(cur.left)
                    temp.append(cur.right)
            
            stack = temp
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution.