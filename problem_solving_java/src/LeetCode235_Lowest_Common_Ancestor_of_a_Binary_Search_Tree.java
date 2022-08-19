public class LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree {
    public static void main(String[] args) {
        LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree_Solution solution = new LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree_Solution();
        TreeNode node = new TreeNode(6, new TreeNode(2, new TreeNode(0), new TreeNode(4, new TreeNode(3), new TreeNode(5))), new TreeNode(8, new TreeNode(7), new TreeNode(9)));
        TreeNode ans = solution.lowestCommonAncestor(node, new TreeNode(0), new TreeNode(3));
        System.out.println(ans);
    }
}

class LeetCode235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree_Solution {public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
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
