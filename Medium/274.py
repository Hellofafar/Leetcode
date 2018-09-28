# ------------------------------
# 274. H-Index
# 
# Description:
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
# Example:
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.
# 
# Version: 1.0
# 09/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        citations.sort(reverse=True)
        
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h += 1
            else:
                break
        
        return h

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Sort at first, and check each citation from high to low.