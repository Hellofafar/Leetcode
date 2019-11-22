# ------------------------------
# 758. Bold Words in String
# 
# Description:
# Given a set of keywords words and a string S, make all appearances of all keywords in S 
# bold. Any letters between <b> and </b> tags become bold.
# 
# The returned string should use the least number of tags possible, and of course the tags 
# should form a valid combination.
# 
# For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". 
# Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
# 
# Note:
# 
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.
# 
# Version: 1.0
# 11/21/19 by Jianfa
# ------------------------------

class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        if not words or not words[0] or not S:
            return S
        
        mark = [False] * len(S)
        
        def markBoldWords(word):
            # if word appear in S, mark the index of appearing letters to True
            length = len(word)
            i = 0
            while S.find(word, i) != -1:
                start = S.find(word, i) # use built-in str.find() function
                for j in range(start, start+length):
                    mark[j] = True
                i = start + 1
                        
        for w in words:
            # mark all bold letters
            markBoldWords(w)
        
        res = ""
        for i in range(len(S)):
            if mark[i] and (i == 0 or not mark[i-1]):
                # if this is bold letter and it's first letter or its last letter is not bold
                res += "<b>"
            res += S[i]
            if mark[i] and (i == len(S) - 1 or not mark[i+1]):
                # if this is bod letter and it's last letter or its next letter is not bold
                res += "</b>"
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Get idea from: https://leetcode.com/problems/bold-words-in-string/discuss/113096/Clean-Java-solution-using-only-boolean-array-and-StringBuilder
# The main idea is to use a boolean array to mark the words at the corresponding positions in S.
# 
# Using built-in str.find() function saves much time comparing checking S[i:i+length] == word
# 
# O(NW) time, W is length of words
# O(N) space