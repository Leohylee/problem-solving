import java.util.ArrayList;
import java.util.List;

public class LeetCode916_Word_Subsets {

    public static void main(String[] args) {
        LeetCode916_Word_Subsets solution = new LeetCode916_Word_Subsets();
        System.out.println(solution.wordSubsets(new String[]{"amazon","apple","facebook","google","leetcode"}, new String[]{"e","o"}));
    }

    private List<String> wordSubsets(String[] A, String[] B) {
        int[] count = new int[26], tmp;
        int i;
        for (String b : B) {
            tmp = counter(b);
            for (i = 0; i < 26; ++i)
                count[i] = Math.max(count[i], tmp[i]);
        }
        List<String> res = new ArrayList<>();
        for (String a : A) {
            tmp = counter(a);
            for (i = 0; i < 26; ++i)
                if (tmp[i] < count[i])
                    break;
            if (i == 26) res.add(a);
        }
        return res;
    }

    private int[] counter(String word) {
        int[] count = new int[26];
        for (char c : word.toCharArray()) count[c - 'a']++;
        return count;
    }

}
