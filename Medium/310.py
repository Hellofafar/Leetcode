# ------------------------------
# 310. Minimum Height Trees
# 
# Description:
# For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is 
# then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees 
# (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of 
# undirected edges (each edge is a pair of labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same 
# as [1, 0] and thus will not appear together in edges.
# 
# Example 1 :
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#         0
#         |
#         1
#        / \
#       2   3 
# Output: [1]
# 
# Example 2 :
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 
# Output: [3, 4]
# 
# Note:
# According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
# 
# Version: 1.0
# 09/25/19 by Jianfa
# ------------------------------

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
            
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            
            leaves = newLeaves
        
        return leaves

# Used for testing
if __name__ == "__main__":
    test = Solution()
    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

# ------------------------------
# Summary:
# Leverage the idea of BFS, but from leaves to root.
# Every time find all the leaves nodes then remove them and go upward to higher level, until at most last two nodes
# Update the list "leaves" every time and return it finally as the root node collection
# "农村包围城市" in Chinese saying
# See: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts