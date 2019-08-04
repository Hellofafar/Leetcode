/* ----------------------------- 
558. Quad Tree Intersection

* Description:
A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft 
and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it 
into four quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent a N * N boolean 
grid. For each node, it will be subdivided into four children nodes until the values in the region it represents 
are all the same. Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if 
the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Note:

1. Both A and B represent grids of size N * N.
2. N is guaranteed to be a power of 2.
3. If you want to know more about the quad tree, you can refer to its wiki.
4. The logic OR operation is defined as this: "A or B" is true if A is true, or if B is true, or if both A and B are true.

* Version: 1.0
* 08/03/19 by Jianfa
* --------------------------- */

/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
    public Node intersect(Node quadTree1, Node quadTree2) {
        if (quadTree1.isLeaf) {
            return quadTree1.val ? quadTree1 : quadTree2;
        }
        
        if (quadTree2.isLeaf) {
            return quadTree2.val ? quadTree2 : quadTree1;
        }
        
        quadTree1.topLeft = intersect(quadTree1.topLeft, quadTree2.topLeft);
        quadTree1.topRight = intersect(quadTree1.topRight, quadTree2.topRight);
        quadTree1.bottomLeft = intersect(quadTree1.bottomLeft, quadTree2.bottomLeft);
        quadTree1.bottomRight = intersect(quadTree1.bottomRight, quadTree2.bottomRight);
        
        if (quadTree1.topLeft.isLeaf && quadTree1.topRight.isLeaf &&
            quadTree1.bottomLeft.isLeaf && quadTree1.bottomRight.isLeaf &&
            quadTree1.topLeft.val == quadTree1.topRight.val &&
            quadTree1.topLeft.val == quadTree1.bottomLeft.val &&
            quadTree1.topLeft.val == quadTree1.bottomRight.val) {
            quadTree1.val = quadTree1.topLeft.val;
            quadTree1.isLeaf = true;
        }
        
        return quadTree1;
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
// Recursive solution.
// https://leetcode.com/problems/quad-tree-intersection/discuss/157532/Java-concise-code-beat-100