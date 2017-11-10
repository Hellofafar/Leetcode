# ------------------------------
# 393. UTF-8 Validation
# 
# Description:
# 
# Version: 1.0
# 11/08/17 by Jianfa
# ------------------------------

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        expected = 0
        for num in data:
            if num > 247:
                return False
            
            binary_num = format(num, 'b')
            binary_num = "0" * (8 - len(binary_num)) + binary_num
            
            count = 0
            for digit in binary_num:
                if digit == "1":
                    count += 1
                else:
                    break
            
            if expected == 0:  # If 10XXXXXX is not expected
                if count >= 2:
                    expected = count - 1
                
                elif count == 1:
                    return False
            
            else:              # If 10XXXXXX is expected
                if count != 1:
                    return False
                
                else:
                    expected -= 1
        
        if expected:
            return False
        
        else:
            return True
            

# ------------------------------
# Summary:
# Set a global variable: expected. When there is a valid encoding start number, set the expected number.
# e.g. 11100010, set expected = 3 - 1 = 2