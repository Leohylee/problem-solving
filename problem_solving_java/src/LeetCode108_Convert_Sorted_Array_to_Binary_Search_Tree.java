public class LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree {

    public static void main(String[] args) {
        LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree solution = new LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree();
        System.out.println(solution.sortedArrayToBST(new int[]{-10,-3,5,9}));
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

    private TreeNode sortedArrayToBST(int[] nums) {
        return recursion(nums, 0, nums.length - 1);
    }

    private TreeNode recursion(int[] nums, int i, int j) {
        if (i > j) return null;
        int m = (i + j) / 2;
        TreeNode node = new TreeNode(nums[m]);
        node.left = recursion(nums, i, m-1);
        node.right = recursion(nums, m+1, j);
        return node;
    }

}
