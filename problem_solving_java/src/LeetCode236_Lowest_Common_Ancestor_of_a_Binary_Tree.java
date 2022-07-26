public class LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree {

    public static void main(String[] args) {
        LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree_Solution solution = new LeetCode236_Lowest_Common_Ancestor_of_a_Binary_Tree_Solution();
        TreeNode_236 node1 = new TreeNode_236(3);
        TreeNode_236 node2 = new TreeNode_236(5);
        TreeNode_236 node3 = new TreeNode_236(1);
        TreeNode_236 node4 = new TreeNode_236(6);
        TreeNode_236 node5 = new TreeNode_236(2);
        TreeNode_236 node6 = new TreeNode_236(0);
        TreeNode_236 node7 = new TreeNode_236(8);
        TreeNode_236 node8 = new TreeNode_236(7);
        TreeNode_236 node9 = new TreeNode_236(4);
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
    private TreeNode_236 ans = null;
    public TreeNode_236 lowestCommonAncestor(TreeNode_236 root, TreeNode_236 p, TreeNode_236 q) {
        if (root == null || root == p || root == q) return root;
        TreeNode_236 x = lowestCommonAncestor(root.left, p, q);
        TreeNode_236 y = lowestCommonAncestor(root.right, p, q);
        return x == null ? y : y == null ? x : root;
    }
}

class TreeNode_236 {
    int val;
    TreeNode_236 left;
    TreeNode_236 right;
    TreeNode_236(int x) { val = x; }
}
