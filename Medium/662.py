# ------------------------------
# 662. Maximum Width of Binary Tree
# 
# Description:
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
# 
# Example 1:
# Input: 
#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# 
# Example 2:
# Input: 
#           1
#          /  
#         3    
#        / \       
#       5   3     
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# 
# Example 3:
# Input: 
#           1
#          / \
#         3   2 
#        /        
#       5      
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# 
# Example 4:
# Input: 
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
# 
# Note: Answer will in the range of 32-bit signed integer.
# 
# Version: 1.0
# 12/23/18 by Jianfa
# ------------------------------

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        children = [(root, 1)]  # A list of (node, id) for current row. id is a counting number to represent node
        width = 0
        
        while children:
            width = max(width, children[-1][1] - children[0][1] + 1)  # The current width is rightmost number minus leftmost number plus one
            
            temp = []
            for node in children:
                if node[0].left:
                    temp.append((node[0].left, node[1] * 2))
                if node[0].right:
                    temp.append((node[0].right, node[1] * 2 + 1))
            
            children = temp
            
        return width

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# BFS solution, but use (node, id) as element to track.