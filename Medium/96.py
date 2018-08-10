# ------------------------------
# 96. Unique Binary Search Trees
# 
# Description:
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
# Example:
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# 
# Version: 1.0
# 08/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        numDict = {0:1, 1:1}
        for i in range(2, n):
            count = 0
            for j in range(1, i+1):  # Count the number of unique BST's when j is the root of BST
                count += numDict[j-1] * numDict[i-j]
            numDict[i] = count
        
        res = 0
        for k in range(1, n+1):
            res += numDict[k-1] * numDict[n-k]
            
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming. I used similar idea as problem 95 at first, which is using 
# recursive idea to calculate. E.g. for num 10, the final result should be the sum
# of number of unique BST's when root is 1, 2, ..., 10. However this solution met
# Time exceed error since there are too many same calculation.
# 
# Still take n = 10 for example. When root is 2, the sum would be same as the sum 
# when root is 9. Actually when calculate the sum, what matters is the number of left
# nodes and number of right nodes. When root is 2, left nodes number is 1 and right
# nodes number is 8, assume there is a map to record the number of Trees when there
# is 1 node or 8 nodes, then the sum would be map[1] * map[8].
# 
# Then I got this idea. For n, I will need to get a map to store all previous number
# result, namely numDict, then I can easily calculate result of numDict[n].