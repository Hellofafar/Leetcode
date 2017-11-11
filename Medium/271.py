# ------------------------------
# 271. Encode and Decode Strings
# 
# Description:
# https://leetcode.com/problems/encode-and-decode-strings/description/
# 
# Version: 1.0
# 11/10/17 by Jianfa
# ------------------------------

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return "".join("%d:" % len(s) + s for s in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        decoded = []
        while(i < len(s)):
            j = s.find(":", i)
            i = j + int(s[i:j]) + 1
            decoded.append(s[j+1:i])
        
        return decoded
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

# ------------------------------
# Summary:
# Follow the same idea from other's solution.
# Use "length:sentence" to encode a sentence, e.g 3:app5:apple9:pineapple, then decode based on every ":s"