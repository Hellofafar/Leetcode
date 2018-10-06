# Given an unordered list inputList, two integers M and L
# Return the largest M sum value of pairs, which contains two number in the inputList that have distance at least L + 1.
# e.g. [8, 5, 12, 3, 4], M = 2, L = 2
# valid pairs are: (8, 3), (8, 4), (5, 4) (there are at least two number between the numbers in the pair)
# Return [11, 12], because M = 2, the largest 2 sum are 8 + 3 = 11 and 8 + 4 = 12

import heapq

def largestPairSum(inputList, M, L):
    if len(inputList) == 0:
        return []
       
    heap = []
    maxSum = []
    for i in range(len(inputList) - L - 1)[::-1]:
        if len(heap) < M:
            heapq.heappush(heap, inputList[i + L + 1])
            heapq.heappush(maxSum, inputList[i] + inputList[i + L + 1])
        
        else:
            currMin = heapq.heappop(heap)
            currMin = min(currMin, inputList[i + L + 1])
            heapq.heappush(heap, currMin)
        
        for k in heap:
            sumMin = heapq.heappop(maxSum)
            heapq.heappush(maxSum, max(sumMin, inputList[i] + k))
    
    return maxSum

numList = [1,2,3,4]
M = 1
L = 1
print(sortPair(numList, M, L))