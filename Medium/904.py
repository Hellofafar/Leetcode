# ------------------------------
# 904. Fruit Into Baskets
# 
# Description:
# In a row of trees, the i-th tree produces fruit with type tree[i].
# You start at any tree of your choice, then repeatedly perform the following steps:
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
# 
# What is the total amount of fruit you can collect with this procedure?
# 
# Example 1:
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# 
# Example 2:
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# 
# Example 3:
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# 
# Example 4:
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
# 
# Version: 1.0
# 10/08/18 by Jianfa
# ------------------------------

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        pt1 = pt2 = 0  # pt1 is fast pointer used to check new type, pt2 is slow pointer used to store latest old type
        res = 0
        
        temp = 1  # Temporal amount of fruits can collect for two types
        for i in range(1, len(tree)):
            if tree[i] == tree[pt1]:
                pt1 = i
                temp += 1
            
            else:
                if pt2 == 0 or tree[i] == tree[pt2]:  # If tree[i] is the second type found or tree[i] is same as tree[pt2]
                    pt2 = i
                    temp += 1
                
                else:
                    res = max(res, temp)  # update res
                    temp = abs(pt1 - pt2) + 1  # abs(pt1 - pt2) is the amount of fruits collected for latest old type
                    pt2 = max(pt1, pt2)
                    pt1 = i
        
        res = max(res, temp)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Two pointer solution