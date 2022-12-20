import java.util.Arrays;

public class LeetCode377_Combination_Sum_IV {

    public static void main(String[] args) {
        LeetCode377_Combination_Sum_IV solution = new LeetCode377_Combination_Sum_IV();
        System.out.println(solution.combinationSum4(new int[]{1,2,3}, 4));
    }

    private int[] dp;

    private int combinationSum4(int[] nums, int target) {
        dp = new int[target + 1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        return helper(nums, target);
    }

    private int helper(int[] nums, int target) {
        if (dp[target] != -1) {
            return dp[target];
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (target >= nums[i]) {
                res += helper(nums, target - nums[i]);
            }
        }
        dp[target] = res;
        return res;
    }

}
