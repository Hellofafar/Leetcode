# ------------------------------
# 515. Find Largest Value in Each Tree Row
# 
# Description:
# You need to find the largest value in each row of a binary tree.
# Example:
# Input: 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# Output: [1, 3, 9]
# 
# Version: 1.0
# 12/22/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        children = [root]
        res = []
        while children:
            temp = []  # Node of next row
            
            largest = -sys.maxsize  # Largest number of this row
            for i in range(len(children)):
                node = children[i]
                largest = max(node.val, largest)
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            res.append(largest)
            children = temp
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution.