# ------------------------------
# 305. Number of Islands II
# 
# Description:
# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation 
# which turns the water at position (row, col) into a land. Given a list of positions to operate, count the 
# number of islands after each addLand operation. An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by 
# water.
# 
# Version: 1.0
# 11/14/17 by Jianfa
# ------------------------------

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        res = []
        if m <= 0 or n <= 0:
            return res
        
        roots = [-1] * m * n
        count = 0
        for pos in positions:
            root = pos[0] * n + pos[1]
            roots[root] = root
            count += 1
            
            for d in dirs:
                x = pos[0] + d[0]
                y = pos[1] + d[1]
                neighbour = x * n + y
                
                if x < 0 or x >= m or y < 0 or y >= n or roots[neighbour] == -1:
                    continue
                
                nbRoot = self.checkLand(roots, neighbour)
                if root != nbRoot:
                    roots[root] = nbRoot
                    root = nbRoot
                    count -= 1
            
            res.append(count)
        
        return res
                    
                
    def checkLand(self, roots, nb):
        while nb != roots[nb]:
            nb = roots[nb]
            
        return nb

# ------------------------------
# Summary:
# Union-find problem.
# Follow "Easiest Java Solution with Explanations" in discuss section.