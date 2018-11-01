/* ----------------------------- 
* 137. Single Number II
*
* Description:
*
* Version: 2.0
* 10/30/18 by Jianfa
* --------------------------- */

class Solution{
    public int singleNumber(int[] nums) {
        int ans = 0;
        for(int i = 0; i < 32; i++) {
            int sum = 0;  // Counter to count the number of 1 appeared at every bit
            for(int j = 0; j < nums.length; j++) {
                if(((nums[j] >> i) & 1) == 1) {  // If the bit i of nums[j] is 1, then sum add 1
                    sum++;
                    sum %= 3;
                }
            }
            if(sum != 0) {
                ans |= sum << i;  // Or operation
            }
        }
        return ans;
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
// Solution from https://leetcode.com/problems/single-number-ii/discuss/43297/Java-O(n)-easy-to-understand-solution-easily-extended-to-any-times-of-occurance
// Cannot solve with python3 because python support over 32 bit of number