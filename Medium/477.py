# ------------------------------
# 477. Total Hamming Distance
# 
# Description:
# The Hamming distance between two integers is the number of positions at which the corresponding 
# bits are different.
# 
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
# 
# Example:
# Input: 4, 14, 2
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# 
# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.
# 
# Version: 1.0
# 10/22/19 by Jianfa
# ------------------------------

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxnum = max(nums)
        K = len(bin(maxnum).split("0b")[1])  # digit number of largest number in binary format
        zeroCount = [0] * K
        oneCount = [0] * K
        
        for n in nums:
            # for every number, check each digit of binary format and add count
            # to zeroCount and oneCount for every digit position
            binary = bin(n).split("0b")[1]
            nLen = len(binary)
            for i in range(nLen):
                if binary[nLen - i - 1] == "1":
                    oneCount[i] += 1
                else:
                    zeroCount[i] += 1
            for i in range(nLen, K):
                zeroCount[i] += 1
        
        res = 0
        for j in range(K):
            # hamming distance on each digit can be calculated by zeroCount[j] * oneCount[j]
            res += zeroCount[j] * oneCount[j] 
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# At first I use brute force solution to get result from all pairs but got TLE
# So I try to count the 1's number and 0's number on every digit respectively and
# sum zeroCount[j] * oneCount[j] for each digit to get result
# 
# O(n * K) time, K is the length of largest number in binary format
# O(K) space
# Similar but with O(1) space can see here: https://leetcode.com/problems/total-hamming-distance/discuss/96226/Java-O(n)-time-O(1)-Space