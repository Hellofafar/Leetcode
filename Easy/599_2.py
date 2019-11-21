# ------------------------------
# 599. Minimum Index Sum of Two Lists
# 
# Description:
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list 
# of favorite restaurants represented by strings.
# 
# You need to help them find out their common interest with the least list index sum. If 
# there is a choice tie between answers, output all of them with no order requirement. You 
# could assume there always exists an answer.
# 
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# 
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# Version: 2.0
# 11/20/19 by Jianfa
# ------------------------------

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurants = {r:i for i, r in enumerate(list1)}
        
        minSum = sys.maxsize
        name = []
        for i, r in enumerate(list2):
            if r in restaurants:
                if i + restaurants[r] < minSum:
                    minSum = i + restaurants[r]
                    name = [r]
                elif i + restaurants[r] == minSum:
                    name.append(r)
        
        return name

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Hashmap solution.
# 
# O(N) time O(N) space