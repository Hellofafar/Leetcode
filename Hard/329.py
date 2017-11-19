# ------------------------------
# 329. Longest Increasing Path in a Matrix
# 
# Description:
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move 
# diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
# 
# Example 1:
# 
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
# 
# Version: 1.0
# 11/16/17 by Jianfa
# ------------------------------

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        global row
        global col
        if not matrix or not matrix[0]:
            return 0
        
        maxLength = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(matrix)
        col = len(matrix[0])
                
        cache = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                maxLength = max(maxLength, self.dfs(matrix, i, j, cache, dirs))
        
        return maxLength
    
    def dfs(self, matrix, i, j, cache, dirs):
        if cache[i][j] != 0:
            return cache[i][j]

        for d in dirs:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < row and y >= 0 and y < col and (x, y) and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(matrix, x, y, cache, dirs))
        
        cache[i][j] += 1
        return cache[i][j]

if __name__ == "__main__":
    test = Solution()
    matrix = [[1,2,3]]

    print(test.longestIncreasingPath(matrix))

# Time Limited
# import collections
# class Solution(object):
#     def longestIncreasingPath(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: int
#         """
#         if not matrix or not matrix[0]:
#             return 0
        
#         maxLength = 0
#         row = len(matrix)
#         col = len(matrix[0])
#         dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
#         isVisited = set()
#         lengthDict = collections.defaultdict(int)
#         for i in range(row):
#             for j in range(col):
#                 distance = 0
                
#                 if (i, j) not in isVisited:
#                     queueList = [(i,j)]
                    
#                     while queueList:
#                         currSize = len(queueList)
#                         for _ in range(currSize):
#                             currCell = queueList.pop(0)
#                             for d in dirs:
#                                 x = currCell[0] + d[0]
#                                 y = currCell[1] + d[1]
                                
#                                 if x >= 0 and x < row and y >= 0 and y < col and (x, y) and \
#                                    matrix[currCell[0]][currCell[1]] < matrix[x][y] and (x, y) not in queueList:
#                                     if (x, y) in lengthDict:
#                                         lengthDict[(i, j)] = max(lengthDict[(i, j)], distance + 1 + lengthDict[(x, y)])
#                                         # lengthDict[currCell] = max(lengthDict[currCell], 1 + lengthDict[(x, y)])
#                                     else:
#                                         queueList.append((x, y))
#                                         isVisited.add((x, y))
                            
                        
#                         distance += 1
                
#                     lengthDict[(i, j)] = max(lengthDict[(i, j)], distance)
        
#         return max(lengthDict.values())

# ------------------------------
# Summary:
# DFS solution. Follow the solution section.
# Question: can a list be global?
# For row, col, and dirs(list), only dirs cannot be considered as a global variable in dfs function.