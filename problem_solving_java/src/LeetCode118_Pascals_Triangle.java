import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LeetCode118_Pascals_Triangle {

    public static void main(String[] args) {
        LeetCode118_Pascals_Triangle solution = new LeetCode118_Pascals_Triangle();
        System.out.println(solution.generate(10));
    }

    private List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 1; i < numRows + 1; i++) {
            res.add(new ArrayList<>(Collections.nCopies(i, 1)));
        }
        if (numRows <= 2) return res;
        for (int i = 2; i < res.size(); i++) {
            List<Integer> prev = res.get(i - 1);
            List<Integer> curr = res.get(i);
            for (int j = 1; j < curr.size() - 1; j++) {
                curr.set(j, prev.get(j - 1) + prev.get(j));
            }
        }
        return res;
    }

}
