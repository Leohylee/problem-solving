public class LeetCode98_Validate_Binary_Search_Tree {
    public static void main(String[] args) {
        LeetCode98_Validate_Binary_Search_Tree_Solution solution = new LeetCode98_Validate_Binary_Search_Tree_Solution();
        TreeNode node = new TreeNode(2, new TreeNode(1), new TreeNode(3, new TreeNode(4), new TreeNode(7)));
        System.out.println(solution.isValidBST(node));
    }
}

class LeetCode98_Validate_Binary_Search_Tree_Solution {
    public boolean isValidBST(TreeNode root) {
        return recursion(root.left, null, root.val) && recursion(root.right, root.val, null);
    }

    private boolean recursion(TreeNode root, Integer x, Integer y) {
        if (root == null) return true;
        if ((x != null && root.val <= x) || (y != null && root.val >= y)) return false;
        return recursion(root.left, x, root.val) && recursion(root.right, root.val, y);
    }
}
