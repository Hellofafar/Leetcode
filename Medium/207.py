# ------------------------------
# 207. Course Schedule
# 
# Description:
# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# 
# Example 1:
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# 
# Version: 1.0
# 08/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            course = pair[0]
            pre = pair[1]
            if matrix[pre][course] == 0:
                inDegree[course] += 1
            matrix[pre][course] = 1
        
        count = 0
        queue = []
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.pop(0)
            count += 1
            for i in range(numCourses):
                if matrix[course][i] != 0:
                    inDegree[i] -= 1
                    if inDegree[i] == 0:
                        queue.append(i)
        
        return count == numCourses

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/course-schedule/discuss/58516/Easy-BFS-Topological-sort-Java