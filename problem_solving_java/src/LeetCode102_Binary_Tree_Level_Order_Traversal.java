import java.util.*;

public class LeetCode102_Binary_Tree_Level_Order_Traversal {

    public static void main(String[] args) {
        LeetCode102_Binary_Tree_Level_Order_Traversal_Solution solution = new LeetCode102_Binary_Tree_Level_Order_Traversal_Solution();
        TreeNode node = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        System.out.println(solution.levelOrder(node));
    }

}

class LeetCode102_Binary_Tree_Level_Order_Traversal_Solution {
    Map<Integer, List<Integer>> levels = new HashMap<>();

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        enterLevel(root, 0);
        levels.forEach((level, vals) -> res.add(level, vals));
        return res;
    }

    private void enterLevel(TreeNode node, Integer level) {
        if (node != null) {
            if (levels.get(level) == null) {
                levels.put(level, new ArrayList<>(Arrays.asList(node.val)));
            } else {
                levels.get(level).add(node.val);
            }
            enterLevel(node.left, level + 1);
            enterLevel(node.right, level + 1);
        }
    }

}

class TreeNode {
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