/* ----------------------------- 
709. To Lower Case

* Description:
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

* Version: 1.0
* 08/06/19 by Jianfa
* --------------------------- */

class Solution {
    public String toLowerCase(String str) {
        if (str != null) {
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                if ((int)c >= 65 && (int)c <= 90) {
                    c = (char)(c + 32);
                } 
                sb.append(c);
            }
            return sb.toString();
        } else {
            return str;
        }    
    }
}

//  Used for testing
public static Main {
    public void main(String[] args) {
        Solution Test = new Solution();
    }
}

// ------------------------------
// Summary:
// 