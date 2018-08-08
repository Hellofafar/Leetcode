# ------------------------------
# 93. Restore IP Addresses
# 
# Description:
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# Version: 1.0
# 08/07/18 by Jianfa
# ------------------------------

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s:
            return res
        
        def backtrack(s, address, res):
            if len(address) == 3:
                if len(s) == 1 or s[0] != '0' and int(s) <= 255:
                    address.append(s)
                    temp = '.'.join(address)
                    res.append(temp)
                    address.pop()

                return

            else:
                if len(s) > 1 and int(s[:1]) <= 255:
                    address.append(s[:1])
                    backtrack(s[1:], address, res)
                    address.pop()

                if len(s) > 2 and s[0] != '0' and int(s[:2]) <= 255:
                    address.append(s[:2])
                    backtrack(s[2:], address, res)
                    address.pop()

                if len(s) > 3 and s[0] != '0' and int(s[:3]) <= 255:
                    address.append(s[:3])
                    backtrack(s[3:], address, res)
                    address.pop()
        
        address = []
        backtrack(s, address, res)
        return res


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Backtrack solution. The tricky point is to design the condition to filter address.
# For example, I got wrong answer at the first time because I outputed the result like '0.1.001.0', but '001' shouldn't be a valid number.
# So I added some condition to eliminate the number start with '0' (except for 0)