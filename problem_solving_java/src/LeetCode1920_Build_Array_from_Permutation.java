// https://leetcode.com/problems/build-array-from-permutation/
//
// Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] =
// nums[nums[i]] for each 0 <= i < nums.length and return it.
//
// A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

public class LeetCode1920_Build_Array_from_Permutation {

    public static void main(String[] args) {
        LeetCode1920_Build_Array_from_Permutation_Solution solution = new LeetCode1920_Build_Array_from_Permutation_Solution();
        System.out.println(solution.buildArray(new int[]{0,2,1,5,3,4}));
    }

}

class LeetCode1920_Build_Array_from_Permutation_Solution {
    public int[] buildArray(int[] nums) {
        int[] news = new int[nums.length];
        int pos = 0;
        for (int num : nums) {
            news[pos] = nums[num];
            pos++;
        }
        return news;
    }
}
