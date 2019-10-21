# ------------------------------
# 900. RLE Iterator
# 
# Description:
# 
# Version: 2.0
# 10/20/19 by Jianfa
# ------------------------------

class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A  # record the rest elements which are not exhausted and their remaining count
        self.cur = 0 # pointer to store the even index i of current first element in the sequence

    def next(self, n: int) -> int:
        if self.cur == len(self.A): # all elements are exhausted
            return -1
        if n <= self.A[self.cur]:   # first unique element has enough number to be exhausted
            self.A[self.cur] -= n
            return self.A[self.cur+1]
        else:                       # first unique element has not enough number to be exhausted, move to next element
            n = n - self.A[self.cur]
            self.cur += 2
            return self.next(n)


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Pointer solution, no need to actually build the array but just do calculation on the count
# 
# O(k) time, O(1) space, k is the number of unique elements to check, worst case n/2