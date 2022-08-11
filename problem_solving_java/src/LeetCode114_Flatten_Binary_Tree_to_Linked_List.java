public class LeetCode114_Flatten_Binary_Tree_to_Linked_List {

    public static void main(String[] args) {
        LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution solution = new LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution();
        TreeNode node = new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)), new TreeNode(5, null, new TreeNode(6)));
        solution.flatten(node);
    }

}

class LeetCode114_Flatten_Binary_Tree_to_Linked_List_Solution {
    private TreeNode ans = null;
    public void flatten(TreeNode root) {
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
