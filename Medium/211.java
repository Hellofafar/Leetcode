/* ----------------------------- 
211. Add and Search Word - Data structure design

* Description:
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


* Version: 1.0
* 08/31/18 by Jianfa
* --------------------------- */

class WordDictionary {
    private WordNode root;
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new WordNode();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        WordNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            if (!node.contains(ch)) {
                node.add(ch);
            }
            node = node.get(ch);
        }
        node.setEnd();
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        WordNode node = root;
        return helper(word, 0, node);
    }
    
    public boolean helper(String word, int index, WordNode node) {
        if (word.length() == index) {
            return node.isEnd();
        }
        if (word.charAt(index) != '.') {
            char ch = word.charAt(index);
            return node.contains(ch) && helper(word, index + 1, node.get(ch));
        }
        else {
            for (int j = 0; j < 26; j++) {
                if ((node.contains((char)('a'+j))) && helper(word, index + 1, node.get((char)('a'+j)))) {
                    return true;
                }
            }
            return false;
        }
    }
}

class WordNode {
    private static int C = 26;
    private WordNode[] links;
    private boolean isEnd;
    
    public WordNode() {
        links = new WordNode[C];
    }
    
    public void add(char ch) {
        links[ch - 'a'] = new WordNode();
    }
    
    public WordNode get(char ch) {
        return links[ch - 'a'];
    }
    
    public boolean contains(char ch) {
        return links[ch - 'a'] != null;
    }
    
    public void setEnd() {
        isEnd = true;
    }
    
    public boolean isEnd() {
        return isEnd;
    }
    
}
/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

//  Used for testing
public static Main {
    public void main(String[] args) {
        Solution Test = new Solution();
    }
}

// ------------------------------
// Summary:
// Get idea from 208 and https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59554/My-simple-and-clean-Java-code
// Need to learn about the simple design way of referenced solution.
// When searching a word, '.' needs to be search recursively to find an existing word.