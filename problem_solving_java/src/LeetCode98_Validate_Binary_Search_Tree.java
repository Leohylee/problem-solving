public class LeetCode98_Validate_Binary_Search_Tree {
    public static void main(String[] args) {
        LeetCode98_Validate_Binary_Search_Tree solution = new LeetCode98_Validate_Binary_Search_Tree();
        TreeNode node = solution.new TreeNode(2, solution.new TreeNode(1), solution.new TreeNode(3, solution.new TreeNode(4), solution.new TreeNode(7)));
        System.out.println(solution.isValidBST(node));
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

    private boolean isValidBST(TreeNode root) {
        return recursion(root.left, null, root.val) && recursion(root.right, root.val, null);
    }

    private boolean recursion(TreeNode root, Integer x, Integer y) {
        if (root == null) return true;
        if ((x != null && root.val <= x) || (y != null && root.val >= y)) return false;
        return recursion(root.left, x, root.val) && recursion(root.right, root.val, y);
    }
}
