# ------------------------------
# 222. Count Complete Tree Nodes
# 
# Description:
# Given a complete binary tree, count the number of nodes.
# Note:
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Example:
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# 
# Version: 1.0
# 09/18/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left:
            return 1
        
        temp = root
        level = 0
        while temp.left:  # Find the deepest level of this tree
            level += 1
            temp = temp.left
        
        # The follow process is based on binary search idea
        # If the deepest level is L, then we check the nodes at level L - 1 to see whether it has children
        # For any node N (note from 0 ~ 2^(L-1)) at level L - 1, 
        #     if not N.left, then no need to check any other node at the right of N, the number of nodes at level L will not be over N * 2.
        #     else if not N.right, then N.left will be the last node at level L - 1
        #     else, continue to check the node at the right of N
        
        low = 0
        high = pow(2, level-1) - 1
        lastLevelNum = pow(2, level)
        while low <= high:
            mid = (low + high) / 2
            path = self.getPath(mid, level - 1)
            node = root
            for i in path:
                node = node.left if i == 0 else node.right

            if not node.left:  # if not node.left, start to check the nodes at the left of node
                high = mid - 1
                lastLevelNum = (mid * 2)
            elif not node.right:  # if not node.right, node.left will be the last node at the last level
                lastLevelNum = (mid * 2) + 1
                print(lastLevelNum)
                break
            else:  # else, continue to check the nodes at the right of node
                low = mid + 1
        
        return pow(2, level) - 1 + lastLevelNum        

    def getPath(self, node, level):  # Get a path to the node
        path = []
        while level:
            direction = node % 2
            if direction % 2 == 0:
                path.insert(0, 0)  # 0 represents left
            else:
                path.insert(0, 1)  # 1 represents right
            
            node = node / 2
            level -= 1
        
        return path

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# See the comments.