import java.util.*;

public class LeetCode102_Binary_Tree_Level_Order_Traversal {

    public static void main(String[] args) {
        LeetCode102_Binary_Tree_Level_Order_Traversal_Solution solution = new LeetCode102_Binary_Tree_Level_Order_Traversal_Solution();
        LeetCode102_TreeNode node = new LeetCode102_TreeNode(3, new LeetCode102_TreeNode(9), new LeetCode102_TreeNode(20, new LeetCode102_TreeNode(15), new LeetCode102_TreeNode(7)));
        System.out.println(solution.levelOrder(node));
    }

}

class LeetCode102_Binary_Tree_Level_Order_Traversal_Solution {
    Map<Integer, List<Integer>> levels = new HashMap<>();

    public List<List<Integer>> levelOrder(LeetCode102_TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        enterLevel(root, 0);
        levels.forEach((level, vals) -> res.add(level, vals));
        return res;
    }

    private void enterLevel(LeetCode102_TreeNode node, Integer level) {
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

class LeetCode102_TreeNode {
    int val;
    LeetCode102_TreeNode left;
    LeetCode102_TreeNode right;
    LeetCode102_TreeNode() {}
    LeetCode102_TreeNode(int val) { this.val = val; }
    LeetCode102_TreeNode(int val, LeetCode102_TreeNode left, LeetCode102_TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}