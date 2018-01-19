# ------------------------------
# 68. Text Justification
# 
# Description:
# Given an array of words and a length L, format the text such that each line has exactly L 
# characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words as you can in 
# each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If the number of 
# spaces on a line do not divide evenly between words, the empty slots on the left will be 
# assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is inserted between 
# words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.
# 
# Version: 1.0
# 01/18/18 by Jianfa
# ------------------------------

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []  # Store words in a line
        line_space = []  # Store the spaces for every interval
        currlen = 0
        
        res = []
        
        for w in words:
            if currlen + len(w) <= maxWidth:
                line.append(w)
                currlen += len(w)
                if currlen == maxWidth:  # So far a new line can be formed with these words
                    space = " "
                    sen = space.join(line)
                    res.append(sen)
                    
                    line = []
                    line_space = []
                    currlen = 0
                
                else:
                    currlen += 1
                
            else:
                word_len = currlen - len(line)  # The length of only characters
                space_len = maxWidth - word_len
                interval_num = len(line) - 1
                
                if len(line) == 1:  # The line with only one word should be left-justified
                    temp = ""
                    for i in range(space_len):
                        temp += " "
                    
                    sen = line[0] + temp
                
                else:
                    base_len = space_len / interval_num
                    temp = ""
                    for i in range(base_len):
                        temp += " "

                    line_space = [temp for j in range(interval_num)]

                    rest = space_len % interval_num
                    for j in range(rest):
                        line_space[j] += " "

                    # Combine the words and spaces
                    sen = ""
                    for x in range(interval_num):
                        sen += line[x]
                        sen += line_space[x]
                    sen += line[-1]
                    
                res.append(sen)

                line = [w]
                currlen = len(w) + 1
                
        if currlen != 0:
            if len(line) == 1:
                space_len = maxWidth - len(line[0])
                temp = ""
                for i in range(space_len):
                    temp += " "
                sen = line[0] + temp
                res.append(sen)
            
            else:
                space_len = maxWidth - currlen
                temp = ""
                for i in range(space_len):
                    temp += " "
                    
                sen = ""
                for x in range(len(line)):
                    sen += line[x]
                    sen += " "
                sen += temp
                res.append(sen)
        
        return res
                

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The basic idea is to build a sentence one by one. As long as the length of a line is not enough
# for adding the new word, then format a new line and add it to the result list.
# One tricky point is when a new line is completed, don't forget to process the new word that is
# not included in this sentence.