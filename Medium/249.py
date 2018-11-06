# ------------------------------
# 249. Group Shifted Strings
# 
# Description:
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
# 
# Example:
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# 
# Version: 1.0
# 11/05/18 by Jianfa
# ------------------------------

class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        group = {}  # hash map to store string model
        
        for s in strings:
            if len(s) == 1:
                group.setdefault('a', []).append(s)  # Add s to string model 'a'
            
            else:
                key = "a"
                for i in range(1, len(s)):
                    diff = (ord(s[i]) - ord(s[i-1])) % 26  # Use difference of neighbour character to indicate the model
                    key += chr(ord('a') + diff)
                
                group.setdefault(key, []).append(s)

        return [group[key] for key in group]


# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use hash map to record the string model and matched strings.