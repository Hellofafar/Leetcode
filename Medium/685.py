# ------------------------------
# 685. Redundant Connection II
# 
# Description:
# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
# 
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# 
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
# 
# Version: 1.0
# 10/09/18 by Jianfa
# ------------------------------

from collections import defaultdict

class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From Solution section.