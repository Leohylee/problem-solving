import java.util.*;

public class LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal {

    public static void main(String[] args) {
        LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal solution = new LeetCode105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal();
        System.out.println(solution.buildTree(new int[]{1,2}, new int[]{2,1}));
    }

    private class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private int[] preorder;
    private int curr = 0;

    private TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        return processNext(inorder);
    }

    private TreeNode processNext(int[] pool) {
        TreeNode root = new TreeNode(preorder[curr]);
        if (pool.length < 1) return null;
        if (pool.length == 1) {
            curr++;
            return root;
        }
        int target = 0;
        while (preorder[curr] != pool[target]) target++;
        curr++;
        root.left = processNext(Arrays.copyOfRange(pool, 0, target));
        if (target + 1 != pool.length) root.right = processNext(Arrays.copyOfRange(pool, target + 1, pool.length));
        return root;
    }

}