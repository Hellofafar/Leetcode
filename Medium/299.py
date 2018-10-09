# ------------------------------
# 299. Bulls and Cows
# 
# Description:
# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
# Please note that both secret number and friend's guess may contain duplicate digits.

# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
# 
# Version: 1.0
# 10/08/18 by Jianfa
# ------------------------------

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        digitMap = {}
        for d in secret:  # First for loop to build a digit map recording the number of digit in secret
            if d in digitMap:
                digitMap[d] += 1
            else:
                digitMap[d] = 1
        
        A = 0
        B = 0
        
        for i in range(len(secret)):  # First for loop to find the bulls
            if guess[i] == secret[i]:
                A += 1
                digitMap[secret[i]] -= 1  # Avoid duplicate when next for loop checking cows
        
        for i in range(len(secret)):  # Second for loop to find the cows
            if guess[i] != secret[i] and digitMap.get(guess[i], 0) > 0:
                B += 1
                digitMap[guess[i]] -= 1
        
        return '%dA%dB' % (A, B)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 