# ------------------------------
# 30. Substring with Concatenation of All Words
# 
# Description:
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
# 
# Example 1:
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# Example 2:
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []
# 
# Version: 2.0
# 10/04/19 by Jianfa
# ------------------------------

from collections import Counter
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if len(words) == 0:
            return res
        
        l = len(words[0]) # Length of single word
        size = len(words) # number of words contained in a substring
        wordDict = Counter(words)
        
        # sliding window(s)
        for i in range(l): # The substring may start from any character of first word
            window = defaultdict(int)
            left = i # window left bound
            curSize = 0 # window size
            for j in range(i, len(s) - l + 1)[::l]:
                word = s[j:j+l]
                if word in wordDict:
                    window[word] += 1
                    curSize += 1
                    while window[word] > wordDict[word]:
                        # word appears more time than expected, shrink window left bound
                        window[s[left:left+l]] -= 1 # Move left pointer to left + l
                        left += l
                        curSize -= 1
                        
                    if curSize == size:
                        res.append(left)
                
                else:
                    #not valid，reset the window
                    window = defaultdict(int)
                    left = j + l
                    curSize = 0
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Sliding windows solution from a 28 ms submission.