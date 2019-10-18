# ------------------------------
# 787. Cheapest Flights Within K Stops
# 
# Description:
# There are n cities connected by m flights. Each fight starts from city u and arrives at 
# v with a price w.
# 
# Now given all the cities and flights, together with starting city src and the destination 
# dst, your task is to find the cheapest price from src to dst with up to k stops. If there 
# is no such route, output -1.
# 
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# 
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# 
# Note:
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
# 
# Version: 1.0
# 10/17/19 by Jianfa
# ------------------------------

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        f = collections.defaultdict(dict)
        for i, j, p in flights:
            f[i][j] = p
        
        priceHeap = [(0, src, K + 1)]
        while priceHeap:
            # get the tuple with cheapest price from the heap,
            # which contains the destination city and the rest available stops
            p, i, k = heapq.heappop(priceHeap)
            
            if i == dst:
                return p
            
            if k > 0:
                for j in f[i]:
                    # add price information of all the cities j that i can reach into heap
                    heapq.heappush(priceHeap, (p + f[i][j], j, k - 1))
        
        return -1

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dijkstra's algorithm idea from https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
# 
# O(E · dkQ + VlogV) time, E is number of edges and V is number of vertex, dkQ is the time to sort in heap