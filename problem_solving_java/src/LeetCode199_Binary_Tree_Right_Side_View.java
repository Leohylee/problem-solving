import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class LeetCode199_Binary_Tree_Right_Side_View {

    public static void main(String[] args) {
        LeetCode199_Binary_Tree_Right_Side_View_Solution solution = new LeetCode199_Binary_Tree_Right_Side_View_Solution();
        TreeNode node = new TreeNode(1, new TreeNode(2, new TreeNode(5), null), new TreeNode(3, null, new TreeNode(4)));
        System.out.println(solution.rightSideView(node));
    }

}

// Not Yet Done!!!!!!
class LeetCode199_Binary_Tree_Right_Side_View_Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        while (!Objects.isNull(root)) {
            res.add(root.val);
            root = root.right;
        }
        return res;
    }
}
