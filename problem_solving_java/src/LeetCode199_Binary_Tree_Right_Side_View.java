import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class LeetCode199_Binary_Tree_Right_Side_View {

    public static void main(String[] args) {
        LeetCode199_Binary_Tree_Right_Side_View solution = new LeetCode199_Binary_Tree_Right_Side_View();
        TreeNode node = solution.new TreeNode(1, solution.new TreeNode(2, solution.new TreeNode(5), null), solution.new TreeNode(3, null, solution.new TreeNode(4)));
        System.out.println(solution.rightSideView(node));
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

    private List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        while (!Objects.isNull(root)) {
            res.add(root.val);
            root = root.right;
        }
        return res;
    }

}