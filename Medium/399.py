# ------------------------------
# 399. Evaluate Division
# 
# Description:
# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is 
# a real number (floating point number). Given some queries, return the answers. If the answer does not 
# exist, return -1.0.
# 
# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> 
# queries , where equations.size() == values.size(), and the values are positive. This represents the 
# equations. Return vector<double>.
# 
# According to the example above:
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero 
# and there is no contradiction.
# 
# Version: 1.0
# 12/09/17 by Jianfa
# ------------------------------

from collections import defaultdict
from itertools import permutations

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (i, j), v in zip(equations, values):
            graph[i][i] = 1
            graph[j][j] = 1
            graph[i][j] = v
            graph[j][i] = 1/v
            
        for k, i, j in permutations(graph, 3):  # Can only be in order k, i, j because of permutations order. k is the component to connect i and j so k should be ordered to check.
            if k in graph[i] and j in graph[k]:
                graph[i][j] = graph[i][k] * graph[k][j]
        
        return [graph[a].get(b, -1.0) for a, b in queries]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Follow the idea from discuss section.
# Floyd–Warshall algorithm
# Notice in the return line, if graph is not defaultdict, it will not work because a may be not the key in graph.