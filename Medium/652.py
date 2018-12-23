# ------------------------------
# 652. Find Duplicate Subtrees
# 
# Description:
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.
# 
# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# 
# The following are two duplicate subtrees:
#       2
#      /
#     4
# and
# 
#     4
# Therefore, you need to return above trees' root in the form of a list.
# 
# Version: 1.0
# 12/22/18 by Jianfa
# ------------------------------

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = collections.Counter()
        ans = []
        
        def collect(root):
            if not root:
                return '#'
            
            serial = '{},{},{}'.format(root.val, collect(root.left), collect(root.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(root)
            
            return serial
        
        collect(root)
        return ans

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# See solution from Solution section: https://leetcode.com/problems/find-duplicate-subtrees/solution/
# Perform a depth-first search, where the recursive function returns the serialization of the tree. 
# At each node, record the result in a map, and analyze the map after to determine duplicate subtrees.