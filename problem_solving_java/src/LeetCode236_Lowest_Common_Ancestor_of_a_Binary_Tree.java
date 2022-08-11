public class LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree {

    public static void main(String[] args) {
        LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree_Solution solution = new LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree_Solution();
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(5);
        TreeNode node3 = new TreeNode(1);
        TreeNode node4 = new TreeNode(6);
        TreeNode node5 = new TreeNode(2);
        TreeNode node6 = new TreeNode(0);
        TreeNode node7 = new TreeNode(8);
        TreeNode node8 = new TreeNode(7);
        TreeNode node9 = new TreeNode(4);
        node1.left = node2;
        node1.right = node3;
        node2.left = node4;
        node2.right = node5;
        node5.left = node8;
        node5.right = node9;
        node3.left = node6;
        node3.right = node7;
        System.out.println(solution.lowestCommonAncestor(node1, node2, node9));
    }

}

class LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree_Solution {
    private TreeNode ans = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode x = lowestCommonAncestor(root.left, p, q);
        TreeNode y = lowestCommonAncestor(root.right, p, q);
        return x == null ? y : y == null ? x : root;
    }
}
