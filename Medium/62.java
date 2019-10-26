// ------------------------------
// 62. Unique Paths
// 
// Description:
// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
// 
// The robot can only move either down or right at any point in time. The robot is trying to reach 
// the bottom-right corner of the grid (marked 'Finish' in the diagram below).
// 
// How many possible unique paths are there?
// 
// Note: m and n will be at most 100.
// 
// Version: 1.0
// 10/09/17 by Jianfa
// ------------------------------

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] grid = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    grid[i][j] = 1;
                }
                else {
                    grid[i][j] = grid[i][j-1] + grid[i-1][j];
                }
            } 
        }
        
        return grid[m-1][n-1];
    }
}

// Used for test
public class Main {
    public static void main(String[] args) {
        int m = 3, n = 7;
        Solution Test = new Solution();

        System.out.println(Test.uniquePaths(m, n));
    }
}

//  ------------------------------
// Summary:
// 