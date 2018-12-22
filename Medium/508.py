# ------------------------------
# 508. Most Frequent Subtree Sum
# 
# Description:
# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
# 
# Examples 1
# Input:
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# 
# Examples 2
# Input:
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.
# 
# Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
# 
# Version: 1.0
# 12/21/18 by Jianfa
# ------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sumDict = {}  # Frequency dictionary
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def countTreeSum(root):
            if not root:
                return 0
            
            left = countTreeSum(root.left)
            right = countTreeSum(root.right)
            currentSum = left + right + root.val
            self.sumDict[currentSum] = self.sumDict.setdefault(currentSum, 0) + 1
            
            return currentSum
        
        self.sumDict = {}
        countTreeSum(root)
        
        pairs = sorted(self.sumDict.items(), key=lambda item: item[1], reverse=True)
        res = []
        maxFreq = pairs[0][1]
        for k, v in pairs:
            if v == maxFreq:
                res.append(k)  # Add all sum number that are most frequent to res list
            else:
                break
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursive solution to calculate sum of subtree from leaf nodes.