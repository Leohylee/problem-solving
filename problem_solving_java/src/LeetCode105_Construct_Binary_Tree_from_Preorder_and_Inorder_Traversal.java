import java.util.*;

public class LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal {

    public static void main(String[] args) {
        LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal_Solution solution = new LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal_Solution();
        System.out.println(solution.buildTree(new int[]{1,2,4,5,3}, new int[]{4,2,5,1,3}));
    }

}

class LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal_Solution {
    int[] preorder;
    int[] inorder;

    public LeetCode105_TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        return processNext(0, 0, new LeetCode105_TreeNode());
    }

    private LeetCode105_TreeNode processNext(int pre, int in, LeetCode105_TreeNode curr) {
        if (preorder[pre] != inorder[in]) {
            curr.val = preorder[pre];

        }
    }

}

class LeetCode105_TreeNode {
    int val;
    LeetCode105_TreeNode left;
    LeetCode105_TreeNode right;
    LeetCode105_TreeNode() {}
    LeetCode105_TreeNode(int val) { this.val = val; }
    LeetCode105_TreeNode(int val, LeetCode105_TreeNode left, LeetCode105_TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}