public class LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree {
    public static void main(String[] args) {
        LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree solution = new LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree();
        TreeNode node = solution.new TreeNode(6, solution.new TreeNode(2, solution.new TreeNode(0), solution.new TreeNode(4, solution.new TreeNode(3), solution.new TreeNode(5))), solution.new TreeNode(8, solution.new TreeNode(7), solution.new TreeNode(9)));
        TreeNode ans = solution.lowestCommonAncestor(node, solution.new TreeNode(0), solution.new TreeNode(3));
        System.out.println(ans);
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

    private TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root.val == p.val || root.val == q.val) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if ((left != null && right != null) && (left.val == p.val && right.val == q.val || left.val == q.val && right.val == p.val)) return root;
        if (left != null && right == null) return left;
        if (right != null && left == null) return right;
        return null;
    }
}