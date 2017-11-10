# ------------------------------
# 418. Sentence Screen Fitting
# 
# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
# 
# Note:
# 
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# 
# Version: 1.0
# 11/07/17 by Jianfa
# ------------------------------

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        string = " ".join(sentence) + " "
        start = 0
        for i in range(rows):
            start += cols
            if string[(start % len(string))] == " ":
                start += 1
            else:
                while (start > 0 and string[(start - 1) % len(string)] != " "):
                    start -= 1
     
        return start // len(string)
                    
                        
if __name__ == "__main__":
    test = Solution()
    sentences = ["f","p","a"]
    rows = 8
    cols = 7

    print(test.wordsTyping(sentences, rows, cols))

# ------------------------------
# Summary:
# "21ms 18 lines Java solution" in discussion section.
