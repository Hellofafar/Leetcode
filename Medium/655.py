# ------------------------------
# 655. Print Binary Tree
# 
# Description:
# Print a binary tree in an m*n 2D string array following these rules:
# 
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# Example 1:
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
#       1
#      / \
#     2   5
#    / 
#   3 
#  / 
# 4 
# Output:
# 
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].
# 
# Version: 1.0
# 12/23/18 by Jianfa
# ------------------------------

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return [[]]
        
        def getHeight(root):
            level = [root]
            height = 0
            
            while level:
                height += 1
                temp = []
                for n in level:
                    if n.left:
                        temp.append(n.left)
                    if n.right:
                        temp.append(n.right)
                
                level = temp
            
            return height
        
        height = getHeight(root)
        
        res = [[""] * (2**height - 1) for _ in range(height)]
        
        self.fillSpace(res, root, 0, len(res[0]) - 1, 0)
        
        return res
        
    def fillSpace(self, res, root, l, r, i):
        if not root or l > r:
            return
        
        col = int((l + r) / 2)
        res[i][col] = str(root.val)
        
        self.fillSpace(res, root.left, l, col - 1, i + 1)
        self.fillSpace(res, root.right, col + 1, r, i + 1)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution.
# Find the height at first.
# The result list should be a matrix with dimensions height * (2^height - 1)
# Start from root, fill the element in the middle of [left, right] with root's value.