# ------------------------------
# 863. All Nodes Distance K in Binary Tree
# 
# Description:
# We are given a binary tree (with root node root), a target node, and an integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the target node.  
# The answer can be returned in any order.
# 
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
# 
# Note:
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# 
# Version: 1.0
# 11/20/19 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.parent = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        toVisit = deque([(target, 0)])
        seen = set()
        while toVisit:
            for i in range(len(toVisit)):
                if toVisit[0][1] == K:
                    # if the first element in the list is K distance from target
                    # all the elements in the list should be at same distance
                    return [node.val for node, dist in toVisit]
                
                node, dist = toVisit.popleft()
                seen.add(node)
                for n in (node.left, node.right, node.parent):
                    if n and n not in seen:
                        toVisit.append((n, dist + 1))
        
        return []

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/
# DFS to add a new link to parent
# Then use BFS start from target node to find K-distance nodes
# 
# Edge case: no nodes found