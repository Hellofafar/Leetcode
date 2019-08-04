/* ----------------------------- 
509. Fibonacci Number

* Description:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

* Version: 1.0
* 08/03/19 by Jianfa
* --------------------------- */

class Solution {
    public int fib(int N) {
        if(N <= 1) {
            return N;
        }
        
        int a = 0, b = 1;
        int sum = 0;
        while(N-- > 1) {
            sum = a + b;
            a = b;
            b = sum;
        }
        
        return sum;
    }
}

//  Used for testing
public static Main {
    public void main(String[] args) {
        Solution Test = new Solution();
    }
}

// ------------------------------
// Summary:
// Iterative solution from https://leetcode.com/problems/fibonacci-number/discuss/215992/Java-Solutions.
// If return fib(N-1) + fib(N-2), it's a recursive solution which cost much time.