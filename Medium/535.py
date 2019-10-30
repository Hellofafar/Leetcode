# ------------------------------
# 535. Encode and Decode TinyURL
# 
# Description:
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as 
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as 
# http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no restriction on 
# how your encode/decode algorithm should work. You just need to ensure that a URL can be 
# encoded to a tiny URL and the tiny URL can be decoded to the original URL.
# 
# Version: 1.0
# 10/29/19 by Jianfa
# ------------------------------

class Codec:
    
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            tinyCode = "".join(random.choice(Codec.alphabet) for _ in range(6))
            if tinyCode not in self.code2url:
                self.url2code[longUrl] = tinyCode
                self.code2url[tinyCode] = longUrl
        
        return self.url2code[longUrl]     

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Idea from: https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
# Use six digits or letters to randomly generate a 6-char string as url
# More idea can be referred to: https://leetcode.com/problems/encode-and-decode-tinyurl/solution/
# e.g. using simple counter, variable-length encoding ...