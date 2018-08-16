# ------------------------------
# 116. Populating Next Right Pointers in Each Node
# 
# Description:
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
        if not root:
            return
        
        prev = root
        cur = None
        while prev.left:
            cur = prev
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            
            prev = prev.left

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From the top voted solution.