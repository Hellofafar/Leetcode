# ------------------------------
# 388. Longest Absolute File Path
# 
# Version: 1.0
# 11/04/17 by Jianfa
# ------------------------------

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split('\n')
        if len(paths) == 0:
            return 0
        
        last_level = 0
        fileSys = {}
        
        root_str = ""
        temp_str = ""
        global_max = 0
        for item in paths:
            current_level = item.count('\t')
            if current_level == 0:
                fileSys[current_level] = item
            else:
                fileSys[current_level] = fileSys[current_level - 1] + '/' + item.split('\t')[-1]
            
            if '.' in item and len(fileSys[current_level]) > global_max:
                global_max = len(fileSys[current_level])
        
        return global_max

# Used for test
if __name__ == "__main__":
    test = Solution()
    input = "a.txt"

    print(test.lengthLongestPath(input))


# ------------------------------
# Summary:
# The idea is to use a dictionary/map to store the path for every level so far. When a file is found just calculate
# the length of its path. Remember to add "/" in the path.
# A trap here is the path itself is a file, don't forget this edge situation.
