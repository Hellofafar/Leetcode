# ------------------------------
# 317. Shortest Distance from All Buildings
# 
# Description:
# 
# Version: 1.0
# 11/15/17 by Jianfa
# ------------------------------

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        rowNum = len(grid)
        colNum = len(grid[0])
        distance = [[0] * colNum for _ in range(rowNum)]
        reach = [[0] * colNum for _ in range(rowNum)]
        buildingNum = 0
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 1:
                    buildingNum += 1    
                    level = 1
                    queueList = [(i, j)]
                    isVisited = [[False] * colNum for _ in range(rowNum)]
                    
                    while queueList:        
                        currSize = len(queueList)
                        for _ in range(currSize):
                            currCell = queueList.pop(0)
                            for dir in dirs:
                                x = currCell[0] + dir[0]
                                y = currCell[1] + dir[1]

                                if(x >= 0 and x < rowNum and y >= 0 and y < colNum and grid[x][y] == 0 and not isVisited[x][y]):
                                    distance[x][y] += level
                                    reach[x][y] += 1
                                    isVisited[x][y] = True
                                    queueList.append((x, y))
                            
                        level += 1
        
        longest = rowNum * colNum * (rowNum + colNum)
        shortest = longest
        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])
        
        return shortest if shortest != longest else -1
        

if __name__ == "__main__":
    test = Solution()
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

    print(test.shortestDistance(grid))

# ------------------------------
# Summary:
# Follow "Java solution with explanation and time complexity analysis" in discuss section
# Two mistake I made here:
# 1) In python, don't use [[0] * num1] * num2 to initialize a two-dimensional list, because all the sub-lists
# refer to same one
# 2) Think about the situation when there is no solution.