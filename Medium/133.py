# ------------------------------
# 133. Clone Graph
# 
# Description:
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# 
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# 
# Visually, the graph looks like the following:
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
# 
# Version: 1.0
# 08/18/18 by Jianfa
# ------------------------------

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.nodeDict = {}
        
    def cloneGraph(self, node):
        if not node:
            return None
        
        if node.label in self.nodeDict:
            return self.nodeDict[node.label]
        
        cloneNode = UndirectedGraphNode(node.label)
        self.nodeDict[node.label] = cloneNode
        for n in node.neighbors:
            cloneNode.neighbors.append(self.cloneGraph(n))
            
        return cloneNode

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# DFS solution from https://leetcode.com/problems/clone-graph/discuss/42309/Depth-First-Simple-Java-Solution