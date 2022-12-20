public class LeetCode114_Flatten_Binary_Tree_to_Linked_List {

    public static void main(String[] args) {
        LeetCode114_Flatten_Binary_Tree_to_Linked_List solution = new LeetCode114_Flatten_Binary_Tree_to_Linked_List();
        TreeNode node = solution.new TreeNode(1, solution.new TreeNode(2, solution.new TreeNode(3), solution.new TreeNode(4)), solution.new TreeNode(5, null, solution.new TreeNode(6)));
        solution.flatten(node);
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

    private TreeNode ans = null;
    private void flatten(TreeNode root) {
        if (root == null) return;
        TreeNode left = root.left;
        TreeNode right = root.right;
        flatten(left);
        flatten(right);
        root.left = null;
        root.right = left;
        TreeNode curr = root;
        while (curr.right != null) {
            curr = curr.right;
        }
        curr.right = right;
    }

}
