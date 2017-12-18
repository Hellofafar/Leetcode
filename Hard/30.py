# ------------------------------
# 30. Substring with Concatenation of All Words
# 
# Description:
# You are given a string, s, and a list of words, words, that are all of the same length. Find 
# all starting indices of substring(s) in s that is a concatenation of each word in words exactly 
# once and without any intervening characters.
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter).
# 
# Version: 1.0
# 12/18/17 by Jianfa
# ------------------------------

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not words:
            return res
        
        total = len(words) * len(words[0])
        single = len(words[0])
        word_dict = {}
        for w in words:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1
        
        i = 0
        while i < len(s) - total + 1:
            substring = s[i:i+total]
            temp_dict = {}
            j = 0
            while j < len(words):
                word = substring[j*single : (j+1) * single]
                if word not in word_dict:
                    break
                    
                if word in temp_dict:
                    temp_dict[word] += 1
                else:
                    temp_dict[word] = 1
                
                if temp_dict[word] > word_dict[word]:
                    break
                
                j += 1
            
            if j == len(words):
                res.append(i)
            
            i += 1
        
        return res
                

# Used for testing
if __name__ == "__main__":
    test = Solution()
    s = "ababaab"
    words = ["ab","ba","ba"]

    print(test.findSubstring(s, words))

# ------------------------------
# Summary:
# Use two maps, one map to record occurence of word in words list, another one to record number 
# of each word in a substring.
# Compare two maps, as long as they are same then current index for substring should be return.