# ------------------------------
# 288. Unique Word Abbreviation
# 
# Description:
# https://leetcode.com/problems/unique-word-abbreviation/description/
# 
# Version: 1.0
# 11/11/17 by Jianfa
# ------------------------------

import collections

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        def buildDict(dictionary):
            d = collections.defaultdict(list)
            for word in dictionary:
                if len(word) > 2:
                    rest = len(word) - 2
                    d[word[0] + word[-1] + str(rest)].append(word)
                
                else:
                    d[word].append(word)
            
            return d
        
        self.dictionary = buildDict(dictionary)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            return True
        
        else:
            rest = len(word) - 2
            
            if word[0] + word[-1] + str(rest) not in self.dictionary:
                return True
            
            elif len(self.dictionary[word[0] + word[-1] + str(rest)]) == 1 and word in self.dictionary[word[0] + word[-1] + str(rest)]:
                return True
    
            else:
                return False
        

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

# ------------------------------
# Summary:
# A trap here is: dictionary includes a word "apple", but you need to check if "adobe" is unique.
# There is only one "axxxe" in the dictionary, but not "adobe", so still return False.
# 
# Another idea about building dictionary is:
# key -> (word[0], len(word) - 2, word[-1])
# if key not in dictionary:
#     dictionary[key] = word
# else:
#     dictionary[key] = ""
# So that it's easier find if the word is unique, according to dictionary[key].