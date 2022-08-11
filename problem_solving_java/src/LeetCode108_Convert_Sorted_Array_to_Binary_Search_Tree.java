public class LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree {

    public static void main(String[] args) {
        LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree_Solution solution = new LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree_Solution();
        System.out.println(solution.sortedArrayToBST(new int[]{-10,-3,5,9}));
    }

}

class LeetCode108_Convert_Sorted_Array_to_Binary_Search_Tree_Solution {
    public TreeNode_108 sortedArrayToBST(int[] nums) {
        return recursion(nums, 0, nums.length - 1);
    }

    private TreeNode_108 recursion(int[] nums, int i, int j) {
        if (i > j) return null;
        int m = (i + j) / 2;
        TreeNode_108 node = new TreeNode_108(nums[m]);
        node.left = recursion(nums, i, m-1);
        node.right = recursion(nums, m+1, j);
        return node;
    }
}

class TreeNode_108 {
     int val;
     TreeNode_108 left;
     TreeNode_108 right;
     TreeNode_108() {}
     TreeNode_108(int val) { this.val = val; }
     TreeNode_108(int val, TreeNode_108 left, TreeNode_108 right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }
