# ------------------------------
# 443. String Compression
# 
# Description:
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# 
# Example 2:
# Input:
# ["a"]
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# Explanation:
# Nothing is replaced.
# 
# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.
# 
# Version: 1.0
# 07/05/18 by Jianfa
# ------------------------------

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        
        count = 0
        char = chars[0]
        curridx = 0 # Position to change character in the list
        for idx, i in enumerate(chars):
            if i == char:
                count += 1
            
            else:
                chars[curridx] = char
                curridx += 1
                char = i
                
                if count > 1:
                    num = str(count)
                    for n in num:
                        chars[curridx] = n # Change the char to number of current character
                        curridx += 1
                
                    count = 1
        
        chars[curridx] = char
        curridx += 1
        if count > 1:
            num = str(count)
            for n in num:
                chars[curridx] = n # Change the char to number of current character
                curridx += 1
                        
        return curridx

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# No need to delete duplicate characters but just change the character in the list.