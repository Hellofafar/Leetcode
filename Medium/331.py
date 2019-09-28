# ------------------------------
# 331. Verify Preorder Serialization of a Binary Tree
# 
# Description:
# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
# 
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# Input: "1,#"
# Output: false
# 
# Example 3:
# Input: "9,#,#,1"
# Output: false
# 
# Version: 1.0
# 09/27/19 by Jianfa
# ------------------------------

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        # diff = outdegree - indegree
        diff = 1
        for n in nodes:
            diff -= 1  # every node bring 1 indegree
            if diff < 0:
                return False
            if n != "#":  # if not null, it brings 2 outdegree
                diff += 2

        return diff == 0

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Math solution idea from: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78551/7-lines-Easy-Java-Solution
# Consider null as leaves, then
# - all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
# - all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
# During building, we record the difference between out degree and in degree diff = outdegree - indegree.
# When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, because it provides two out degrees. 
# If a serialization is correct, diff should never be negative and diff will be zero when finished.
# 
# Stack solution: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78560/Simple-Python-solution-using-stack.-With-Explanation.
# When you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#". For example,
# preorder = 1,2,3,#,#,#,#
# Pass 1: stack = [1]
# Pass 2: stack = [1,2]
# Pass 3: stack = [1,2,3]
# Pass 4: stack = [1,2,3,#]
# Pass 5: stack = [1,2,3,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,2,#]
# Pass 6: stack = [1,2,#,#] -> two #s on top so pop them and replace top with #. -> stack = [1,#]
# Pass 7: stack = [1,#,#] -> two #s on top so pop them and replace top with #. -> stack = [#]
# 
# If there is only one # on stack at the end of the string then return True else return False.

