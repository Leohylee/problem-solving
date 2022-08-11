public class LeetCode300_Longest_Increasing_Subsequence {

    public static void main(String[] args) {
        LeetCode300_Longest_Increasing_Subsequence_Solution solution = new LeetCode300_Longest_Increasing_Subsequence_Solution();
        System.out.println(solution.lengthOfLIS(new int[]{10,9,2,5,3,7,101,1,18}));
    }

}

class LeetCode300_Longest_Increasing_Subsequence_Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int num : nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < num) {
                    i = m + 1;
                } else {
                    j = m;
                }
            }
            tails[i] = num;
            if (i == size) size++;
        }
        return size;
    }
}
