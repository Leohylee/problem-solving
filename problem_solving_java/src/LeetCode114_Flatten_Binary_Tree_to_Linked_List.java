public class LeetCode114_Flatten_Binary_Tree_to_Linked_List {

    public static void main(String[] args) {
        LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution solution = new LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution();
        TreeNode_114 node = new TreeNode_114(1, new TreeNode_114(2, new TreeNode_114(3), new TreeNode_114(4)), new TreeNode_114(5, null, new TreeNode_114(6)));
        solution.flatten(node);
    }

}

class LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution {
    private TreeNode_114 ans = null;
    public void flatten(TreeNode_114 root) {
        if (root == null) return;
        TreeNode_114 left = root.left;
        TreeNode_114 right = root.right;
        flatten(left);
        flatten(right);
        root.left = null;
        root.right = left;
        TreeNode_114 curr = root;
        while (curr.right != null) {
            curr = curr.right;
        }
        curr.right = right;
    }
}

class TreeNode_114 {
    int val;
    TreeNode_114 left;
    TreeNode_114 right;
    TreeNode_114() {}
    TreeNode_114(int val) { this.val = val; }
    TreeNode_114(int val, TreeNode_114 left, TreeNode_114 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
